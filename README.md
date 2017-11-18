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

Note that when running locally, the app server URL is typically
`localhost:5000`; see details below.

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

Note that this will inform you of the URL you can use to hit your local server
instance (typically `localhost:5000`).

## Tests

To run tests, just simply run the included tests script from the root directory
of this project:

```
./tests.sh
```

## Type-checking

To run type-checks via (mypy)[http://mypy-lang.org/], run the included script
from the root directory of this project:

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

## Design and implementation principles

* Verbosity and strict data structures are favored over simplicity and data
    assumptions. As an example, a simple but structured `LatLng` class is used
    to pass around latitude-longitude information, instead of either a bare
    2-tuple of `(lat, lng)` or an unstructured dict (even if it has the same
    `lat` and `lng` keys and values). This type of design choice is made
    throughout the repo.
    * On a related note, Python 3 type hints are used throughout the codebase,
    and [mypy](http://mypy-lang.org/) is used for type checking.
* According to the constraints and nature of the context for this project,
    third-party libraries are used for receiving input requests and responding
    to them, but NOT for making the outgoing requests to the actual external
    geocoding APIs (this is implemented purely using the Python Standard
    Library, using included packages such as `urlparse` and `json`).
* Test-driven development was/is heavily used in this project.
* Where applicable, before implementing core business logic, tests and skeleton
    outlines (via thorough comments) are written to outline both the expected
    behavior AND the actual implementation of the core logic. This can be seen
    in the commit/PR history; in particular, you'll see that there are several
    test-focused and "skeleton"-focused PRs (which, again, provide skeleton
    outlines via comments without any code), only then followed by
    "implementation" PRs. This is a useful approach for delineating the flow,
    requirements, and behavior of the project and its features, and is
    especially useful for avoiding sinking time into coding only to find that
    changes and rewrites are needed due to unforeseen circumstances (that would
    have been caught by more careful planning).
