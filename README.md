# fluffy-spork

[![Coverage Status](https://coveralls.io/repos/github/gflaherty/fluffy-spork/badge.svg?branch=master)](https://coveralls.io/github/gflaherty/fluffy-spork?branch=master)

[![codecov](https://codecov.io/gh/gflaherty/fluffy-spork/branch/master/graph/badge.svg)](https://codecov.io/gh/gflaherty/fluffy-spork)

# How to
Coverage with pytest-cov:

(The `-c` option is very important. The script creates a `coverage.xml` file which it won't regenerate
if you don't include that flag - resulting in stale coverage data)
```
python -m pytest --cov=. -v -s
../codecov.sh -c -t 76a9880f-fb41-4aa4-b548-de441cde39da
```

```
git add "**/*.py"
```

Must have installed:
```
sudo pip install pytest
sudo pip install pytest-cov
```

