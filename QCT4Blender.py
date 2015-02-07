import bpy

class QCTBlender(bpy.types.Operator):
 bl_idname = "qct.import_topology"
 bl_label = "Import Topology"
 
 filepath = bpy.props.StringProperty(subtype="FILE_PATH")
 
 def execute(self, context):
  print("QCT4Blender Executed")
  print("Opening File: " + self.filepath)
  return{'FINISHED'}
  
 def invoke(self, context, event):
  print("QCT4Blender Invoked")
  context.window_manager.fileselect_add(self)
  return {'RUNNING_MODAL'}
  
def register():
 print("Registering Classes")
 bpy.utils.register_class(QCTBlender) # add the defined Operator to the built-in collection
 
def unregister():
 print("Deregistering Classes")
 bpy.utils.register_class(QCTBlender) # add the defined Operator to the built-in collection

if __name__ == "main":
 register()

#For Debugging as text script
register()

bl_info = \
{
"name" : "Import QC Topology",
"author" : "Matthew M L Mills <mjohnmills@gmail.com>",
"version" : (0, 0, 0),
"blender" : (2, 69, 0),
"location" : "View 3D > Object Mode > Tool Shelf",
"description" :
"Import a QCT .top File",
"warning" : "",
"wiki_url" : "",
"tracker_url" : "",
"category" : "Add Mesh",
}