## AzothApp
AzothApp is a RestfulAPI built to deploy **tgBoost** and other AI models for inference of physical properties of chemical compounds involved in atmospheric chemistry.

## Motivation
[**tgBoost**](https://pubs.rsc.org/en/content/articlelanding/2022/ea/d1ea00090j#!divRelatedContent&articles) is a ML model inferring  <em>T</em><sub>g</sub> of monomer organic molecules from molecular structures expressed as molecular embeddings. AzothApp provides the RestfulAPI of tgBoost to be integrated in frontend development and for online users of the model.

## Requirements
* **Python >=3.7.0, <3.8** (Python 2.x is [not supported](http://www.python3statement.org/))
* [uvicorn](https://www.uvicorn.org/) >=0.20.0,<0.30.0
* [fastapi](https://fastapi.tiangolo.com/) >=0.88.0,<1.0.0
* [python-multipart](https://pypi.org/project/python-multipart/) =0.0.5,<0.1.0
* [pydantic](https://docs.pydantic.dev/) >=1.10.5,<1.12.0
* [typing_extensions](https://pypi.org/project/typing-extensions/) >=4.2.0,<5.0.0
* [loguru](https://github.com/Delgan/loguru) >=0.5.3,<1.0.0
* [importlib_metadata](https://github.com/python/importlib_metadata) < 5.0>
* [RDKit](http://www.rdkit.org/docs/Install.html)
* [mol2vec](https://github.com/samoturk/mol2vec)
* [tgapp](https://pypi.org/project/tgapp/)

## Build status
Build status of continus integration i.e. travis, appveyor etc. Ex. - 

[![Build Status](https://travis-ci.org/akashnimare/foco.svg?branch=master)](https://travis-ci.org/akashnimare/foco)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/akashnimare/foco?branch=master&svg=true)](https://ci.appveyor.com/project/akashnimare/foco/branch/master)

#### Documentation
Details on the statistical analysis performed to develop **tgBoost** are found in the supporting [article](https://pubs.rsc.org/en/content/articlelanding/2022/ea/d1ea00090j#!divRelatedContent&articles). 

### How to cite?

✨ 🍰 ✨

```bib
@Article{D1EA00090J,
author ="Galeazzo, Tommaso and Shiraiwa, Manabu",
title  ="Predicting glass transition temperature and melting point of organic compounds via machine learning and molecular embeddings",
journal  ="Environ. Sci.: Atmos.",
year  ="2022",
volume  ="2",
issue  ="3",
pages  ="362-374",
publisher  ="RSC",
doi  ="10.1039/D1EA00090J",
url  ="http://dx.doi.org/10.1039/D1EA00090J"
}
```

## Contribute
Contact at tommaso.galeazzo@gmail.com

## Credits
Initial development was supported by [AirUCI](https://airuci.uci.edu), Irvine, CA.

## License
BSD 3-clause © [Tommaso Galeazzo](https://www.tmsglz.com)