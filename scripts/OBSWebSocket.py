import json
from hashlib import sha256
from base64 import b64encode

class OBSWebSocket:
	def __init__(self, parentComp):
		self.parentComp = parentComp
		self.websocket = op('websocket')
		
		self.parentComp.par.Connected = False
	
	def Identify(self, data):		
		response = {
			'op': 1,
			'd': {
				'rpcVersion': 1,
				'eventSubscriptions': self.getSubscriptionBitmask()
			}
		}

		if 'authentication' in data:
			secret = b64encode(
				sha256(
					(self.parentComp.par.Password + data['authentication']['salt']).encode()
				).digest()
			)
		
			auth = b64encode(
				sha256(
					(secret.decode() + data['authentication']['challenge']).encode()
				).digest()
			).decode()

			response['d']['authentication'] = auth

		self.websocket.sendText(json.dumps(response))
	
	def Reidentify(self):
		message = {
			'eventSubscriptions': self.getSubscriptionBitmask()
		}

		self.websocket.sendText(json.dumps(message))
	
	def getSubscriptionBitmask(self):
		bitmask = 0

		for n in range(11):
			bitmask |= 1 << n
		
		if self.parentComp.par.Includeinputvolumemeters:
			bitmask |= 1 << 16
		if self.parentComp.par.Includeinputactivestatechanged:
			bitmask |= 1 << 17
		if self.parentComp.par.Includeinputshowstatechanged:
			bitmask |= 1 << 18
		if self.parentComp.par.Includesceneitemtransformchanged:
			bitmask |= 1 << 19
		
		return bitmask
	
	def HandleEvent(self, data):
		name = data['eventType']
		hasData = 'eventData' in data
	
		if name == 'ExitStarted':
			self.parentComp.par.Connected = False
			return
		elif not hasData:
			return
	
		data = data['eventData']
		func = None
	
		try:
			func = getattr(self, name)
		except:
			print(f'OBSWebSocket - No event function to call for {name}')
	
		if callable(func):
			param = name.lower().capitalize()
			func(data, param)
	
	'''
	CONFIG EVENTS
	'''
	
	def CurrentSceneCollectionChanging(self, data, param):
		self.parentComp.par[param] = data['sceneCollectionName']
	
	def CurrentSceneCollectionChanged(self, data, param):
		self.parentComp.par[param] = data['sceneCollectionName']
	
	def SceneCollectionListChanged(self, data, param):
		self.parentComp.par[param] = data['sceneCollections']
	
	def CurrentProfileChanging(self, data, param):
		self.parentComp.par[param] = data['profileName']
	
	def CurrentProfileChanged(self, data, param):
		self.parentComp.par[param] = data['profileName']
	
	def ProfileListChanged(self, data, param):
		self.parentComp.par[param] = data['profiles']
	
	'''
	SCENE EVENTS
	'''
	
	def SceneCreated(self, data, param):
		self.parentComp.par[param] = data
	
	def SceneRemoved(self, data, param):
		self.parentComp.par[param] = data
	
	def SceneNameChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def CurrentProgramSceneChanged(self, data, param):
		self.parentComp.par[param] = data['sceneName']
	
	def CurrentPreviewSceneChanged(self, data, param):
		self.parentComp.par[param] = data['sceneName']
	
	def SceneListChanged(self, data, param):
		self.parentComp.par[param] = data['scenes']
	
	'''
	INPUT EVENTS
	'''
	
	def InputCreated(self, data, param):
		self.parentComp.par[param] = data
	
	def InputRemoved(self, data, param):
		self.parentComp.par[param] = data['inputName']
	
	def InputNameChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def InputActiveStateChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def InputShowStateChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def InputMuteStateChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def InputVolumeChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def InputAudioBalanceChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def InputAudioSyncOffsetChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def InputAudioTracksChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def InputAudioMonitorTypeChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def InputVolumeMeters(self, data, param):
		self.parentComp.par[param] = data['inputs']
	
	'''
	TRANSITION EVENTS
	'''
	
	def CurrentSceneTransitionChanged(self, data, param):
		self.parentComp.par[param] = data['transitionName']
	
	def CurrentSceneTransitionDurationChanged(self, data, param):
		self.parentComp.par[param] = data['transitionDuration']
	
	def SceneTransitionStarted(self, data, param):
		self.parentComp.par[param] = data['transitionName']
	
	def SceneTransitionEnded(self, data, param):
		self.parentComp.par[param] = data['transitionName']
	
	def SceneTransitionVideoEnded(self, data, param):
		self.parentComp.par[param] = data['transitionName']
	
	'''
	FILTER EVENTS
	'''
	
	def SourceFilterListReindexed(self, data, param):
		self.parentComp.par[param] = data
	
	def SourceFilterCreated(self, data, param):
		self.parentComp.par[param] = data
	
	def SourceFilterRemoved(self, data, param):
		self.parentComp.par[param] = data
	
	def SourceFilterNameChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def SourceFilterEnableStateChanged(self, data, param):
		self.parentComp.par[param] = data
	
	'''
	SCENE ITEM EVENTS
	'''
	
	def SceneItemCreated(self, data, param):
		self.parentComp.par[param] = data
	
	def SceneItemRemoved(self, data, param):
		self.parentComp.par[param] = data
	
	def SceneItemListReindexed(self, data, param):
		self.parentComp.par[param] = data
	
	def SceneItemEnableStateChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def SceneItemLockStateChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def SceneItemSelected(self, data, param):
		self.parentComp.par[param] = data
	
	def SceneItemTransformChanged(self, data, param):
		self.parentComp.par[param] = data
	
	'''
	OUTPUT EVENTS
	'''
	
	def StreamStateChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def RecordStateChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def ReplayBufferStateChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def VirtualcamStateChanged(self, data, param):
		self.parentComp.par[param] = data
	
	def ReplayBufferSaved(self, data, param):
		self.parentComp.par[param] = data['savedReplayPath']
	
	'''
	MEDIA INPUT EVENTS
	'''
	
	def MediaInputPlaybackStarted(self, data, param):
		self.parentComp.par[param] = data['inputName']
	
	def MediaInputPlaybackEnded(self, data, param):
		self.parentComp.par[param] = data['inputName']
	
	def MediaInputActionTriggered(self, data, param):
		self.parentComp.par[param] = data
	
	'''
	UI EVENTS
	'''
	
	def StudioModeStateChanged(self, data, param):
		self.parentComp.par[param] = data['studioModeEnabled']
	
	def ScreenshotSaved(self, data, param):
		self.parentComp.par[param] = data['savedScreenshotPath']