Error Handling
==============

Note that the async api methods return an object of type FaceitApiError
if the request was not successful. To distinguish between a successful
response and an error, you can easily use the object as a boolean expression:

.. code-block:: python

    games = await api.games()
    if games:
        print('success')
    else:
        print('error')
