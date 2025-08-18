# Generates sketch lines for vertical holes in a Fusion 360 sketch to be well printed in a FFF(FDM) 3D printer.

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    try:
        app=adsk.core.Application.get()
        ui=app.userInterface
        design=app.activeProduct

        circles=[]
        for selection in ui.activeSelections:
            sel_entity=selection.entity
            if sel_entity.objectType != adsk.fusion.SketchCircle.classType():
                ui.messageBox('Not a circle! Skipping.')
                continue
            circles.append(adsk.fusion.SketchCircle.cast(sel_entity))

        if len(circles) == 0:
            ui.messageBox('No circles selected!')
            return

        for circle in circles:
            sketch=circle.parentSketch
            drawings(circle, sketch)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


def drawings(circle, sketch):
    ui=None
    try:
        app=adsk.core.Application.get()
        ui=app.userInterface
        design=app.activeProduct

        center=circle.centerSketchPoint
        radius=circle.radius

        lines=sketch.sketchCurves.sketchLines
        start_point=adsk.core.Point3D.create(center.geometry.x, center.geometry.y, center.geometry.z)
        end_point=adsk.core.Point3D.create(center.geometry.x, center.geometry.y+radius+0.3, center.geometry.z)
        center_line=lines.addByTwoPoints(start_point, end_point)
        center_line.isConstruction=True

        drop_line1_end=adsk.core.Point3D.create(center.geometry.x+radius+1, center.geometry.y+radius+0.3, center.geometry.z)
        drop_line1=lines.addByTwoPoints(end_point, drop_line1_end)

        drop_line2_end=adsk.core.Point3D.create(center.geometry.x+radius-1, center.geometry.y+radius+0.3, center.geometry.z)
        drop_line2=lines.addByTwoPoints(end_point, drop_line2_end)

        dimensions=sketch.sketchDimensions
        constraints=sketch.geometricConstraints

        constraints.addVertical(center_line)
        constraints.addCoincident(center_line.startSketchPoint, center)
        constraints.addCoincident(drop_line1.startSketchPoint, center_line.endSketchPoint)
        constraints.addCoincident(drop_line1.endSketchPoint, circle)
        constraints.addCoincident(drop_line2.startSketchPoint, center_line.endSketchPoint)
        constraints.addCoincident(drop_line2.endSketchPoint, circle)
        constraints.addTangent(drop_line1, circle)
        constraints.addTangent(drop_line2, circle)
        constraints.addSymmetry(drop_line1, drop_line2, center_line)

        dimension_point=adsk.core.Point3D.create(center.geometry.x-0.1, center.geometry.y+radius-0.1, center.geometry.z)
        angle_betw_lines=dimensions.addAngularDimension(center_line, drop_line2, dimension_point)
        angle_betw_lines.parameter.expression='125 deg'

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
