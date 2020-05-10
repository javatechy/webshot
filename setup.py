import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='webshot',  
     version='0.1',
     scripts=['webshot'] ,
     author="Deepak Kumar",
     author_email="deepak.kumar.iet@gmail.com",
     description="A Webpage screenshot utility package for testing images similiarity",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/javatechy/webshot",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )