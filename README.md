# ml-serving

ML engineering tutorial.

1. Setup:
   1. Install and setup Docker.
   2. Initialise build and serve environments using the given Python versions.

        ```bash
        pyenv install 3.12.2
        PYENV_VERSION=3.12.2 pyenv exec python -m venv .venv-build
        PYENV_VERSION=3.12.2 pyenv exec python -m venv .venv-serve
        ```

   3. Install the respective requirements in their environments.

        ```bash
        source .venv-build/bin/activate
        pip install -r scripts/build/requirements.txt
        deactivate
        source .venv-serve/bin/activate
        pip install -r scripts/serve/requirements.txt
        deactivate
        ```

   4. You can also install the development requirements (either in one or both of the pre-made environments, or create a new one). Then run `pre-commit install`.
2. Test out functionality locally:
   1. Build the dataset and train the model (in the build environment):
      1. `python -m scripts.build`
   2. Serve the model (in the serve environment):
      1. `python -m scripts.serve` or `python -m flask --app scripts.serve.__main__ run`
      2. Or you can use it in debug mode, where it will automatically restart the server after changes have been made: `python -m flask --app scripts.serve.__main__ run --debug`
   3. Send data to the server to query the model:

       ```bash
       curl -X POST -H "Content-Type: application/json" localhost:8080/predict -d @artifacts/data/X.json
       ```

3. Version the dataset and models:
   1. Create a Google Drive (or Google Drive folder) for the data that will be created.
   2. Run `dvc init`
   3. Point to your remote storage: `dvc remote add --default myremote gdrive://<GDRIVE-ID>`
   4. Tell it to not show some warning messages: `dvc remote modify myremote gdrive_acknowledge_abuse true`
   5. Track data and model files:
      1. `dvc add artifacts/data/*`
      2. `dvc add artifacts/models/*`
      3. In DVC adding does staging and committing together
      4. Follow the instructions to Git track these changes
   6. Push the data changes to your remote: `dvc push`
   7. Make a change to the dataset:
      1. Change the `random_state` in `scripts/build/dataset.py` then rerun the build script: `deactivate && source .venv-build/bin/activate && python -m scripts.build`
      2. Track the changes:
         1. `dvc add artifacts/data/X.json artifacts/data/y.json`
         2. `dvc add artifacts/models/model.joblib`
         3. Follow Git instructions
   8. Play with `playground.ipynb`, changing the git SHAs to retrieve different file versions.
4. Dockering
   1. Build the building image:
      1. `docker build -t ml-serving-build:v0 -f scripts/build/Dockerfile .`
   2. Run the building image:
      1. `docker run -v ~/PATH/TO/ml-serving/docker-artifacts:/home/user/workdir/artifacts ml-serving-build:v0`
   3. Build the serving image:
      1. `docker build -t ml-serving-serve:v0 -f scripts/serve/Dockerfile .`
   4. Run the serving image:
      1. `docker run -v ~/PATH/TO/ml-serving/docker-artifacts:/home/user/workdir/artifacts -p 8080:8080 ml-serving-serve:v0`
