# Geocoder

Simple REST API server for geocoding addresses, implemented in Python.

## Setup

1. This project requires Project 3.6+ (3.6.3 recommended). See the
    [official Python downloads](https://www.python.org/downloads/) to get this
    installed on your system.

2. Install `virtualenv` on your system (optionally using the `sudo` prefix):
    ```
    [sudo] pip3 install virtualenv
    ```

3. Install project dependencies by running the following command from the root
    directory of this project:
    ```
    ./install_dependencies.sh
    ```

4. Set API keys for the third-party geocoding APIs that are used by this library
    (currently, Google Maps Geocoding API and HERE Geocoder API). To do so,
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

## Type-checking

To run type-checks, run the included script from the root directory of this project:

```
./type_check.sh
```

## virtualenv

As a note, if you'd like to contribute or debug this project any further, you'll
need to drop into the appropriate `virtualenv` manually before changing/updating
requirements, running code manually (outside of the supplied scripts), etc. To
do so, from the root directory of this project, run:

```
source .venv/bin/activate
```

On most systems, you should now see `(.venv)` prepended to your command
prompt. Proceed as you wish now!
