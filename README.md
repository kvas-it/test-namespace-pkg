# test-namespace-pkg

A test to verify if `pkg_resources.declare_namespace` is necessary in
order for both `foo.bar` and `foo.baz` to be importable in the following
setup:

* A package `foo-bar` contains `foo/__init__.py` and `foo/bar/__init__.py`.
* A package `foo-baz` contains `foo/__init__.py` and `foo/baz/__init__.py`.
* We install both packages and try to import `foo.bar` and `foo.baz`.

## Usage

To run the test:

	$ ./run test

To clean up:

	$ ./run clean
