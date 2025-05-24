from airflow import settings
from airflow.auth.managers.fab.fab_auth_manager import FabAuthManager
from flask_appbuilder.security.sqla.models import User, Role
from flask_bcrypt import generate_password_hash

def create_airflow_user():
    # Initialize the FAB authentication manager
    security_manager = FabAuthManager(settings.Session)

    # Create a session
    with settings.Session() as session:
        # Check if Admin role exists, create if not
        admin_role = session.query(Role).filter(Role.name == "Admin").first()
        if not admin_role:
            admin_role = Role(name="Admin")
            session.add(admin_role)
            session.commit()
            # Assign default Admin permissions
            security_manager.bulk_sync_roles([
                {
                    "role": "Admin",
                    "perms": [(perm, view) for perm, view in security_manager.get_all_permissions()]
                }
            ])
            print("Created Admin role with full permissions")

        # Check if user already exists
        existing_user = session.query(User).filter(User.username == "admin").first()
        if existing_user:
            print("User 'admin' already exists")
            return

        # Create user
        user = User(
            username="admin",
            first_name="Admin",
            last_name="User",
            email="admin@example.com",
            roles=[admin_role],
            password=generate_password_hash("admin"),  # Use a secure password
            active=True
        )
        session.add(user)
        session.commit()
        print("User 'admin' created successfully with Admin role")

if __name__ == "__main__":
    create_airflow_user()