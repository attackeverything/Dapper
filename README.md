# SOCAlgoTestPlatform

**Developer Names**: Declan Young, Nathan Uy, Aidan Mariglia, Ben Dubois

**Date of project start**: 16 September 2024

**Project Description**:Battery state of charge (SOC) estimation is challenging, requiring specialized algorithms. Standardized testing is necessary to determine which of the hundreds of SOC estimation approaches proposed yearly are the best. This project will expand upon an existing, early stage online SOC estimation algorithm testing tool. The tool is Matlab based, receives submissions through a Google form, and tests algorithms in serial on a server at McMaster. This approach is not scalable
though since testing each algorithm takes an hour or more and the software regularly crashes due to unhandled errors from the submitted algorithms. The project objectives are to create: (1) A cloud based software implementation which can test multiple algorithm submissions in parallel, (2) A secure algorithm submission portal which prevents malware attacks etc., (3) A web interface which reports and compares algorithm performance (see Kaggle as an example), (4) A robust version of the
model testing software which can handle any error. These software improvements will allow the testing tool to be scaled up to having several hundred active users.

The folders and files for this project are as follows:

docs - Documentation for the project

refs - Reference material used for the project, including papers

src - Source code

test - Test cases
