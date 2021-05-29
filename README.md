# Simple Entity Recognition Demo


### Installation

This app needs `poetry` for package management, which you can install from [here](https://python-poetry.org/docs/#installation).

```bash
# Assuming you have make tools installed on you computer.
make install
```

### Run

Use the following command to start a flask debug instance.

```bash
make run
```

You may use the following command to test the service, which sends post a new text corpus to `/api/english`:

```bash
make demo
```

### Test

Use the following command to run tests with `pytest`

```bash
make test
```
