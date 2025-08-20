import "vars.just"
import "configs.just"
import "docker.just"

# Make all actions needed for run homework from zero.
app-i-docker-i-run: d-up

# Make all actions needed for purge homework related data.
app-i-docker-i-purge: d-purge
