"""Small helper to initialize the database and create a sample project.

Run this script during development to create the SQLite DB and a sample project entry.
"""
import sys
from pentestai.core.database import init_db, SessionLocal
from pentestai.models.entities import Project


def main():
    init_db()
    if SessionLocal is None:
        print("SessionLocal not configured; init_db may have failed.")
        sys.exit(1)

    db = SessionLocal()
    try:
        # create a sample project if none exists
        existing = db.query(Project).filter(Project.name == "sample").one_or_none()
        if not existing:
            p = Project(name="sample", description="Sample project created by init_db script")
            db.add(p)
            db.commit()
            print("Created sample project: sample")
        else:
            print("Sample project already exists")
    finally:
        db.close()


if __name__ == "__main__":
    main()
