try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
setup(
      name = "newsman-api-python",
      version = "1.2.3",
      description = "Newsman API 1.2 - Python Client",
      author = "Newsman - Catalin Constantin",
      url = "https://github.com/Newsman/newsman-api-python",
      packages = ["newsman"],
      install_requires = [],
      zip_safe = True,
      license = "BSD",
      classifiers = (
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English, Romanian",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",            
        ) 
    )
