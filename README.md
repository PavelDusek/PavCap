# PavCap
Pavel Dusek's simple library for REDCap (https://www.project-redcap.org/) API communication in Python.

# Usage
```
import PavCap
pc = PavCap.Project( token = 'your-project-token', url = 'your-site.url/api/' )
pc.listFields()
pc.listIds()
```
