bl_info = {
    "name": "Material Duplicates Replacement",
    "author": "Timothé Lapetite",
    "version": (1, 0),
    "blender": (3, 3, 0),
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

def replace_material_duplicates():
    # Get all objects in the scene
    objects = bpy.data.objects

    # Regular expression pattern to match material duplicates
    pattern = r"(.+)\.[0-9][0-9][0-9]"

    # Go through all objects
    for obj in objects:
        # Go through all material slots of the object
        for slot in obj.material_slots:
            # Get the material of the slot
            material = slot.material

            # Check if the material is a duplicate
            if re.match(pattern, material.name):
                # Get the name of the original material
                original_name = re.sub(pattern, r"\1", material.name)

                # Get the original material
                original_material = bpy.data.materials.get(original_name)

                # Replace the duplicate material with the original material
                if original_material:
                    slot.material = original_material

class ReplaceMaterialDuplicates(bpy.types.Operator):
    """Replace All Material Duplicates"""
    bl_idname = "object.replace_material_duplicates"
    bl_label = "Replace All Material Duplicates"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        replace_material_duplicates()
        return {'FINISHED'}

class MaterialPanel(bpy.types.Panel):
    bl_label = "Material Utils"
    bl_idname = "OBJECT_PT_material_utils"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "world"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.replace_material_duplicates")

def register():
    bpy.utils.register_class(ReplaceMaterialDuplicates)
    bpy.utils.register_class(MaterialPanel)
    bpy.app.handlers.depsgraph_update_post.append(replace_material_duplicates)

def unregister():
    bpy.utils.unregister_class(ReplaceMaterialDuplicates)
    bpy.utils.unregister_class(MaterialPanel)
    bpy.app.handlers.depsgraph_update_post.remove(replace_material_duplicates)

if __name__ == "__main__":
    register()
