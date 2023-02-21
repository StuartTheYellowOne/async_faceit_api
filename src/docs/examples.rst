Examples
========

If you dont already got a loop in your programm you need to create one.
Here is a basic example which will search players by the username and
prints out a dict witch the nicknames and player_ids:

.. literalinclude:: ../../examples/example.py
   :language: python
   :linenos:

Its recomended to store the api_key somewhere safe (e.g in an .env file)!

Here is another example on how you can implement the api by subclassing and using a ".env" file.
Note that this example also shows you how you can use "asyncio.gather()" to increase the speed of your code,
if you want to do multiple independent requests.

.. literalinclude:: ../../examples/subclassing.py
   :language: python
   :linenos:
