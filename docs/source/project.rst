
Project
=======

Before we can do anything with the framework we need to create a project.
A project is simply a package containing a ``settings.py`` module.
In addition you need an entrypoint script.

This can be auto-generated using the ``demosys-admin`` command:

.. code:: shell

    demosys-admin createproject myproject

This will generate the following structure:

.. code-block:: shell

    myproject
    └── settings.py
    manage.py

- ``settings.py`` is the settings for your project with good defaults. See :doc:`settings` for more info.
- ``manage.py`` is an executable script for running your project

Effects
^^^^^^^

It's normally a good idea to put effect packages inside the project package as
this protects you from package name collisions. It's of course also fine
to put them at the same level as your project or even have them in separate
repositories and install them as packages thought ``pip``.

manage.py
^^^^^^^^^

The ``manage.py`` script is an alternative entry point to ``demosys-admin``.
Both can perform the same commands. The main purpose of ``demosys-admin``
is to initially have an entry point to the commands creating
a projects and effects when we don't have a ``manage.py`` yet.

Management Commands
^^^^^^^^^^^^^^^^^^^

Custom commands can be added to your project. This can be useful when you need additional tooling
or whatever you could imagine would be useful to run from ``manage.py``.

Creating a new command is fairly straight forward. Inside your project package, create
the ``management/commands/`` directories. Inside the commands directory we can add commands.
Let's add the command ``test``.

The project structure (excluding effects) would look something like:

.. code-block:: shell

    myproject
    └── settings.py
    └── management
        └── commands
            └── test.py

Notice we added a ``test`` module inside ``commands``. The name of the module will be
name of the command. We can reach it by:

.. code-block:: shell

    ./manage.py test

Our test command would look like this:

.. code-block:: shell

    from demosys.core.management.base import BaseCommand

    class Command(BaseCommand):
        help = "Test command"

        def add_arguments(self, parser):
            parser.add_argument("message", help="A message")

        def handle(self, *args, **options):
            print("The message was:", options['message'])

- ``add_arguments`` exposes a standard argparser we can add arguments for the command.
- ``handle`` is the actual command logic were the parsed arguments are passed in
- If the parameters to the command do not meet the requirements for the parser,
  a standard arparse help will be printed to the terminal
- The command class must be named ``Command`` and there can only be one command per module

This is pretty much identical to who management commands are done in django.
