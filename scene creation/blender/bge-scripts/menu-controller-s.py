import bge
cont = bge.logic.getCurrentController()
own = cont.owner #owner of the controller is the active object (try print(own))
scene = bge.logic.getCurrentScene() #this sets scene as a bge.types.KX_Scene object



hover = cont.sensors["MouseOver"]
leftClick = cont.sensors["leftClick"] #note leftclick shold be set to 'tap'(?)
deselect = cont.sensors["deselect"]


if leftClick.positive and hover.positive:

	own['selectedprep']= True
	for child in own.children:
		
		child.color = (.3,.3,.3,.3)

	for obj in scene.objects:
		if obj != own:
			obj['selectedprep']=False
			for child in obj.children:
				child.color = (1,1,1,1)

	

if deselect.positive:
	own['selectedprep']= False
	for child in own.children:
		child.color = (1,1,1,1)
