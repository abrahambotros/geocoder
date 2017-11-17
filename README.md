# Geocoder

Simple REST API for geocoding addresses, implemented in Python.

## Setup

1. This project requires Project 3.6+ (3.6.3 recommended). See the
    [official Python downloads](https://www.python.org/downloads/) to get this
    installed on your system.

2. Install `virtualenv` on your system (optionally using the `sudo` prefix):
    ```
    [sudo] pip3 install virtualenv
    ```

3. From the root directory of this project, enter this project's `virtualenv`:
    ```
    source .venv/bin/activate
    ```
    On most systems, you should now see `(.venv)` prepended to your command
    prompt.

4. From the root directory of this project, install this project's dependencies:
    ```
    pip3 install -r requirements.txt
    ```
5. Set API keys for the third-party geocoding APIs that are used by this library
    (currently, Google Maps Geocoding API and here Geocoder API). To do so,
    create a new `.env` file in the root directory of this project, and define
    it as follows, inserting your own API keys:
    ```
    GMAPS_API_KEY="<Your Google Maps API key>"
    HERE_APP_ID="<Your HERE app ID>"
    HERE_APP_CODE="<Your HERE app code>"
    ```


## Run

After the setup above, all you need to do to start the app server is run the included script from
the root directory of this project!

```
./run.sh
```

## Tests

To run tests, just simply run the included tests script from the root directory of this project:

```
./tests.sh
```
