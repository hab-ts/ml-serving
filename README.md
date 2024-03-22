# ml-serving

ML engineering tutorial.

1. Setup:
   1. Clone this repo locally:

        ```bash
        git clone https://github.com/hab-ts/ml-serving.git
        ```

   2. Install and setup Docker.
   3. Update gcloud CLI: `gcloud components update`
   4. Initialise build and serve environments using the given Python versions.

        ```bash
        pyenv install 3.12.2
        PYENV_VERSION=3.12.2 pyenv exec python -m venv .venv-build
        PYENV_VERSION=3.12.2 pyenv exec python -m venv .venv-serve
        ```

   5. Install the respective requirements in their environments.

        ```bash
        source .venv-build/bin/activate
        pip install -r scripts/build/requirements.txt
        deactivate
        source .venv-serve/bin/activate
        pip install -r scripts/serve/requirements.txt
        deactivate
        ```

   6. You can also install the development requirements (either in one or both of the pre-made environments, or create a new one). Then run `pre-commit install`.
2. Run through code:
   1. More info on logging: [Modern Python logging](https://www.youtube.com/watch?v=9L77QExPmI0).
   2. Creating applications in Python with Flask: [Documentation](https://flask.palletsprojects.com/en/3.0.x/).
3. Test out functionality locally:
   1. Build the dataset and train the model (in the build environment):
      1. `python -m scripts.build`
   2. Serve the model (in the serve environment):
      1. `python -m scripts.serve` or `python -m flask --app scripts.serve.__main__ run`
      2. Or you can use it in debug mode, where it will automatically restart the server after changes have been made: `python -m flask --app scripts.serve.__main__ run --debug`
   3. Send data to the server to query the model:

       ```bash
       curl -X POST -H "Content-Type: application/json" localhost:8080/predict -d @artifacts/data/X.json
       ```

4. Version the dataset and models:
   1. Create a Google Drive (or Google Drive folder) for the data that will be created.
   2. Create a new branch, e.g. `git checkout -b your-name`
   3. Run `dvc init`
   4. Point to your remote storage: `dvc remote add --default myremote gdrive://<GDRIVE-ID>`
   5. Tell it to not show some warning messages: `dvc remote modify myremote gdrive_acknowledge_abuse true`
   6. Track data and model files:
      1. `dvc add artifacts/data/*`
      2. `dvc add artifacts/models/*`
      3. In DVC adding does staging and committing together
      4. Follow the instructions to Git track these changes
   7. Push the data changes to your remote: `dvc push`
   8. Make a change to the dataset:
      1. Change the `random_state` in `scripts/build/dataset.py` then rerun the build script: `deactivate && source .venv-build/bin/activate && python -m scripts.build`
      2. Track the changes:
         1. `dvc add artifacts/data/X.json artifacts/data/y.json`
         2. `dvc add artifacts/models/model.joblib`
         3. Follow Git instructions
   9. Play with `playground.ipynb`, changing the git SHAs to retrieve different file versions.
5. Dockering:
   1. Initialise Docker daemon (open the app).
   2. Look through Dockerfiles.
   3. Build the building image:
      1. `docker build -t ml-serving-build:v0 -f scripts/build/Dockerfile .`
   4. Run the building image:
      1. `docker run -v ~/PATH/TO/ml-serving/docker-artifacts:/home/user/workdir/artifacts ml-serving-build:v0`
   5. Build the serving image:
      1. `docker build -t ml-serving-serve:v0 -f scripts/serve/Dockerfile .`
   6. Run the serving image:
      1. `docker run -v ~/PATH/TO/ml-serving/docker-artifacts:/home/user/workdir/artifacts -p 8080:8080 ml-serving-serve:v0`
   7. Rerun the curl command.
   8. Close the container: `docker stop ID`
6. Deploying to an endpoint:
   1. Go to your favourite Google Cloud project, e.g. [camresp-ml-vms](https://console.cloud.google.com/home/dashboard?project=camresp-ml-vms).
   2. Set your project to that: `gcloud config set project project-name`
   3. Go to the [Artifacts Registry product](https://console.cloud.google.com/artifacts?project=camresp-ml-vms).
   4. Create a repository with your name, and location `europe-west2`.
   5. Set up authentication to Docker repositories in your region: `gcloud auth configure-docker europe-west2-docker.pkg.dev`
   6. Change the name of the serving image to point to the new Docker repository:

    ```bash
    docker tag ml-serving-serve:v0 europe-west2-docker.pkg.dev/PROJECT-NAME/testrepo/ml-serving-serve:v0
    ```

    Check this with `docker images`

    > Note: if you do not specify the repository, it defaults to [DockerHub](https://hub.docker.com/).

   7. Push the serving image: `docker push europe-west2-docker.pkg.dev/PROJECT-NAME/REPO-NAME/ml-serving-serve:v0`
   8. How to deploy to a VM (which would be more apt for a model building image)
   9. How to deploy to Cloud Run, e.g. adding health check
   10. [DOESN'T WORK AS CLOUD RUN CANNOT BE INITIALISED WITH GOOGLE CLOUD BUCKET MOUNT] but you get the idea
7. The process of building Docker images, pushing to remote container registry, and deploying can be done automatically in GitHub Actions CI/CD. Give it a go!
