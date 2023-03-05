# Mapping
1. `catkin_make`
2. `source ./devel/setup.sh` or `source ./devel/setup.zsh` if you are using zsh
3. `roslaunch mapping mapping.launch` for mapping
# Localization
1. `catkin_make`
2. `source ./devel/setup.sh` or `source ./devel/setup.zsh` if you are using zsh
3. `roslaunch localization localization.launch` for localization


Problem:

The initial pose is not aligned with the map's origin. This might be resolved by global localization service provided by amcl.