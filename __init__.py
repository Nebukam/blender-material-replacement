bl_info = {
    "name": "Material Replacement",
    "author": "Timothé Lapetite",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "location": "Preferences > Add-ons",
    "description": "Replaces materials created during import with suffixes (in the form of '.###') with existing materials with the same name and no suffix.",
    "warning": "",
    "support": "COMMUNITY",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"
}

import bpy
import re

def replace_material_duplicates(objects, cleanup):
    duplicates = []
    
    # Iterate through the objects
    for obj in objects:
        # Iterate through the materials of the object
        for mat_slot in obj.material_slots:
            mat = mat_slot.material
            # Check if the material name matches the duplicate material pattern
            if re.match('.*\.\d{3}$', mat.name):
                # Strip off the ending dot and digits to get the original material name
                original_name = mat.name[:-4]
                # Try to get the original material
                original_mat = bpy.data.materials.get(original_name)
                if original_mat is not None:
                    # If the original material exists, set the material slot to use it
                    mat_slot.material = original_mat
                    # Add the duplicate material to the list to be deleted later
                    if mat not in duplicates:
                        duplicates.append(mat)
    
    # Delete all the duplicate materials
    if cleanup:
        for mat in duplicates:
            bpy.data.materials.remove(mat)

class FindAndReplaceAll(bpy.types.Operator):
    """Replace All Material Duplicates"""
    bl_idname = "object.find_and_replace_in_scene"
    bl_label = "Run on Scene"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        replace_material_duplicates(bpy.data.objects, True)
        return {'FINISHED'}

class FindAndReplaceInSelection(bpy.types.Operator):
    """Replace Material Duplicates within Selection"""
    bl_idname = "object.find_and_replace_in_selection"
    bl_label = "Run on Selection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        replace_material_duplicates(bpy.context.selected_objects, False) #no cleanup in case removed mats are used outside selection
        return {'FINISHED'}

class MaterialPanel(bpy.types.Panel):
    bl_label = "Material Duplicates Clean-up"
    bl_idname = "SCENE_PT_material_utils"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout        
        # Add a button to apply the function to all objects in the scene
        layout.operator("object.find_and_replace_in_scene")
        # Add a button to apply the function to the active selection
        layout.operator("object.find_and_replace_in_selection")

def register():
    bpy.utils.register_class(FindAndReplaceAll)
    bpy.utils.register_class(FindAndReplaceInSelection)
    bpy.utils.register_class(MaterialPanel)

def unregister():
    bpy.utils.unregister_class(FindAndReplaceAll)
    bpy.utils.unregister_class(FindAndReplaceInSelection)
    bpy.utils.unregister_class(MaterialPanel)

if __name__ == "__main__":
    register()