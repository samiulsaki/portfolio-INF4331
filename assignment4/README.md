# ---------------------------------------------------------------------
## In order to run any files inside the ___ "test"___ directory, first 
## install the ___ "integrators"___ package using the setup.py intsallation 
## tool. The setup.py will also compile cython_integrator.pys before 
## the package installation in done. Once the installation is done, 
## it should be okay to run the tests from the ___ "test"___ directory 
## without any further problem.
#  -------------------------------------------------------------------- 

### Please install the entire ___integrators___  package with:
	
	python setup.py install --user
	
### Inside the ___"test"___ directory, run the tests as:
	
	e.g. python test_integrator.py
	
