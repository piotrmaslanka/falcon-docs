falcon-docs
========

[![Build Status](https://travis-ci.org/piotrmaslanka/falcon-docs.svg)](https://travis-ci.org/piotrmaslanka/falcon-docs)
[![Maintainability](https://api.codeclimate.com/v1/badges/698296b5954d7cbdd0dc/maintainability)](https://codeclimate.com/github/piotrmaslanka/falcon-docs/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/698296b5954d7cbdd0dc/test_coverage)](https://codeclimate.com/github/piotrmaslanka/falcon-docs/test_coverage)
[![Issue Count](https://codeclimate.com/github/piotrmaslanka/falcon-docs/badges/issue_count.svg)](https://codeclimate.com/github/piotrmaslanka/falcon-docs)
[![PyPI](https://img.shields.io/pypi/pyversions/falcon-docs.svg)](https://pypi.python.org/pypi/falcon-docs)
[![PyPI version](https://badge.fury.io/py/falcon-docs.svg)](https://badge.fury.io/py/falcon-docs)
[![PyPI](https://img.shields.io/pypi/implementation/falcon-docs.svg)](https://pypi.python.org/pypi/falcon-docs)

Usage:

```python
import falcon
from falcondocs import FalconDocumentationResource, FalconDocumentationRouter

api = falcon.API(router=FalconDocumentationRouter())
FalconDocumentationResource(api).register(u'/docs')
```

