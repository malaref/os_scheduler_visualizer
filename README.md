# Welcome to OS Scheduler Visualizer!
OS Scheduler Visualizer is a helper tool for visualizing the output of the OS scheduler project

## Usage

### Requirements
* Python 3
* Python dependencies that can be installed by `pip` using `pip install --user --upgrade -r requirements.txt`

#### Command-line Interface

Run the command-line interface using the command `python os_scheduler_visualizer.py SCHEDULER_LOG_PATH FIGURE_PATH` where `SCHEDULER_LOG_PATH` is the path to the scheduler log and `FIGURE_PATH` is the path (name) of the image to be rendered.

#### Web-based Interface

A mini-sever is also available to give a more convenient way of using the tool. It can be used by running `python server.py`. This was mainly implemented to be hosted online (see next section).

## Hosted Version

For extra convenience, a version of the tool is [hosted on Heroku](https://os-scheduler-visualizer.herokuapp.com/). It only requires a browser to use it, i.e., no Python or dependencies!

## License and Guarantees

This is a free open-source tool and it is offered _as is_ with no guarantees whatsoever (see LICENSE for details).

**Use it at your own risk!**
