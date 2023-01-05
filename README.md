# blender-material-replacement ![version](https://img.shields.io/badge/version-1.0.0-darkgreen) ![license](https://img.shields.io/badge/license-MIT-black.svg)
## A straighforward blender add-on that replaces materials created during import with suffixes (in the form of '.###') with existing materials with the same name and no suffix.  
  
Long story short, will swap `MyMatID.001`, `MyMatID.010`, `MyMatID.012` for **`MyMatID`** if it exists, and remove the others. If no "main" material is found, the script simply ignore the material.  
  
Support Blender 3.3.x, may work with older version, don't know, haven't tested.


--
## Install
Simply download this repo as a .ZIP and follow [blender's instructions](https://docs.blender.org/manual/en/latest/editors/preferences/addons.html) to install the add-on.

## Use
Once installed and enabled, a new panel will be available in the **scene properties tab** under **Material Duplicate Clean-up**, simply click the button `Run on Scene` to clean-up all materials in the scene, or `Run on Selection` to only affect the active selection.  
  
*Note that `Run on Selection` does not remove replaced duplicate, as sometimes dupes are used outside of the selection, resulting in loss of data.*

### Limitations
Running this on the scene loop through all objects, one by one, and for each object loops through all material within the .blend file, one by one. As such, if you have a very very complex scene with either tons of objects, or tons of materials, or both, you are very likely to experience small freezes. It's not ideal, but it works :)