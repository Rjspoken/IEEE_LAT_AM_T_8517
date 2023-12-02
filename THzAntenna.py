# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2017.0.0

# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project14")
oProject.InsertDesign("HFSS", "HFSSDesign3", "DrivenModal", "")
oDesign = oProject.SetActiveDesign("HFSSDesign3")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.SetModelUnits(
	[
		"NAME:Units Parameter",
		"Units:="		, "um",
		"Rescale:="		, False
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-0.9um",
		"YStart:="		, "-1um",
		"ZStart:="		, "0um",
		"Width:="		, "1.8um",
		"Height:="		, "2.1um",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rectangle1:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "100um"
				],
				[
					"NAME:YSize",
					"Value:="		, "100um"
				],
				[
					"NAME:Position",
					"X:="			, "-50um",
					"Y:="			, "-50um",
					"Z:="			, "0um"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-50um",
		"YPosition:="		, "-50um",
		"ZPosition:="		, "0um",
		"XSize:="		, "100um",
		"YSize:="		, "100um",
		"ZSize:="		, "757523175um"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Box1:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:ZSize",
					"Value:="		, "10um"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Box1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Material",
					"Value:="		, "\"Rogers RT/duroid 6010/6010LM (tm)\""
				],
				[
					"NAME:Color",
					"R:="			, 255,
					"G:="			, 255,
					"B:="			, 0
				],
				[
					"NAME:Transparent",
					"Value:="		, 0.52
				]
			]
		]
	])
oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "0um",
		"YCenter:="		, "0um",
		"ZCenter:="		, "10um",
		"Radius:="		, "40um",
		"WhichAxis:="		, "Z",
		"NumSegments:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Circle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Circle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 128,
					"G:="			, 0,
					"B:="			, 0
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 128,
					"G:="			, 64,
					"B:="			, 64
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Ground"
				]
			]
		]
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "40um",
		"YStart:="		, "-5um",
		"ZStart:="		, "0um",
		"Width:="		, "10um",
		"Height:="		, "10um",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rectangle1:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "39um",
					"Y:="			, "-5um",
					"Z:="			, "10um"
				],
				[
					"NAME:XSize",
					"Value:="		, "11um"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "feed"
				]
			]
		]
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Circle1,feed"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "0um",
		"YCenter:="		, "0um",
		"ZCenter:="		, "10um",
		"Radius:="		, "33.5410196624968um",
		"WhichAxis:="		, "Z",
		"NumSegments:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Circle2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Circle2:CreateCircle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Radius",
					"Value:="		, "30um"
				]
			]
		]
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "Circle1",
		"Tool Parts:="		, "Circle2"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-30um",
		"YStart:="		, "-5um",
		"ZStart:="		, "0um",
		"Width:="		, "60um",
		"Height:="		, "10um",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rectangle1:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-30um",
					"Y:="			, "-2um",
					"Z:="			, "10um"
				],
				[
					"NAME:YSize",
					"Value:="		, "4um"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "CentreLine"
				]
			]
		]
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Circle1,CentreLine"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-45um",
		"YStart:="		, "-20um",
		"ZStart:="		, "0um",
		"Width:="		, "-3um",
		"Height:="		, "36um",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rectangle1:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-47um",
					"Y:="			, "-15um",
					"Z:="			, "10um"
				],
				[
					"NAME:XSize",
					"Value:="		, "4um"
				],
				[
					"NAME:YSize",
					"Value:="		, "30um"
				]
			]
		]
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Circle1,Rectangle1"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
