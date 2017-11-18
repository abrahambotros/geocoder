# Geocoder

Simple REST API server for geocoding addresses, implemented in Python.

#### Inputs

This simple server accepts HTTP `GET` requests to its root route (`/`), with an
`address` URL parameter indicating the address string that should be geocoded.
Thus, if you wanted to get the geocoded data for some location in San Francisco,
CA, you might make the following request to this server:

```
<app URL>/?address=123+Somewhere+St,+San+Francisco,+CA>
```

#### Geocoding overview

The actual geocoding is done via requests to third-party geocoding APIs. In
particular, this app first tries querying the
[Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/start),
followed by the [HERE Geocoder API](https://developer.here.com/documentation/geocoder/topics/quick-start.html).
You must provide your access keys to these APIs as described below in a `.env`
file (we did not include our own keys here to avoid them getting abused!).

#### Outputs

If the geocoding is successful, this server will write back to the client a
simple JSON object of the form:

```
{
    "data": {
        "lat": <float value indicating the latitude of the input address>,
        "lng": <float value indicating the latitude of the input address>,
    },
}
```

If there were otherwise any errors in the geocoding process, this server will
instead write back to the client a JSON object of the form (where `errors` is a
list):

```
{
    "errors": [
        {
            "status": <integer HTTP error code, following standard conventions>,
            "title": <string providing a summary of the error>
        },
        ...,
    ],
}
```

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

After the setup above, all you need to do to start the app server is run the
included script from the root directory of this project!

```
./run.sh
```

## Tests

To run tests, just simply run the included tests script from the root directory
of this project:

```
./tests.sh
```

## Type-checking

To run type-checks, run the included script from the root directory of this
project:

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
