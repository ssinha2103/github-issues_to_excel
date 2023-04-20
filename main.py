import sys
import app

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <milestone_number> <access_token> <repo_name>")
        sys.exit(1)
    if len(sys.argv) > 4:
        app.run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    if len(sys.argv) > 3:
        app.run(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        app.run(sys.argv[1], sys.argv[2])


