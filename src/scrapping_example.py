# Package docummentation

# https://github.com/twintproject/twint/blob/master/README.md

## Example
# Import the module
import twint

# Set up TWINT config
c = twint.Config()
c.Username = "now"
c.Search = "Fruit"

# Start search
twint.run.Search(c)
