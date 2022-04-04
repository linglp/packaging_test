import toml
data = toml.load("pyproject.toml")

# Modify field
data['tool']['poetry']['version']='$RELEASE_VERSION'
#override and save changes
f = open("pyproject.toml",'w')
toml.dump(data, f)
f.close()