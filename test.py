from ast import For


packages = [
  {'name': 'package1', 'version': '1.0.0', 'deprecated': False, 'year': 2020},
  {'name': 'package2', 'version': '1.0.0', 'deprecated': False, 'year': 2020},
  {'name': 'package3', 'version': '1.0.0', 'deprecated': True, 'year': 2020},
]

# map for each package

class Package:
  def __init__(self, name, version, deprecated, year):
    self.name = name
    self.version = version
    self.deprecated = deprecated
    self.year = year
    self.message = self.should_be_changed()
  def should_be_changed(self):
    v = self.deprecated and (2022 - self.year) > 1
    if(v):
      return 'should be changed'
    else:
      return 'should not be changed'

p = Package('package1', '1.0.0', False, 2020)
print(p.message)

for package in packages:
  p+= Package(package['name'], package['version'], package['deprecated'], package['year'])