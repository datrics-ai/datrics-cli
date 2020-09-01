
class ShowDataService:

    @staticmethod
    def show_projects(projects):
        print("   id   title".format())
        for project in projects:
            print("{:5d}   {}".format(project['id'], project['title']))