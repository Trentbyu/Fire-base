
# db.collection('persons').add({'name': 'john', 'age': 48})

    # ADD
#  set document with know id
# res = db.collection('Place').document('barcelona').set({
#     'lat': 41.3851, 'long': 2.1734,
#     'weather': 'great',
#     'landmarks': [
#         'guadí park',
#         'gaudí church',
#         'gaudí everything'
#     ]
# })


# #   UPDATE
# res = db.collection('Place').document('barcelona').update({
#     'weather': 'bee'
# })

# db.collection('Place').document('rome').set({
#     'where_to_go': firestore.ArrayUnion(['colosseum'])
# })

#     # REMOVE
# db.collection('Place').document('rome').update({
#     'where_to_go': firestore.ArrayRemove(
#         ['vatican_city', 'trastevere']
# )})


# # DELETE
# db.collection.document('rome').delete()
# db.collection.document('barcelona').update({
#     'weather': firestore.DELETE_FIELD})


# QUERY
# db.collection('places').where('long', '>', 2.1734).get()

