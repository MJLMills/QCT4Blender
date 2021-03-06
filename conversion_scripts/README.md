# Conversion Scripts

The included Blender Add-On functions on topological data provided in the XML format described in the Rhorix [paper](https://www.researchgate.net/publication/319407440_Rhorix_An_interface_between_quantum_chemical_topology_and_the_3D_graphics_program_blender).
However, no topological analysis program currently provides output in this format.
There is therefore a need for tools which can convert the output of existing programs into the XML format.
The code in this directory provides the ability to convert output from AIMAll and MORPHY/IRIS into Rhorix input.
In addition, code for general use and for writing the XML files has been abstracted into a set of Perl modules.
This facilitates the future addition of converters for other QCT analysis programs.

## Scripts

### AIMAll Conversion

mgpviz2top.pl - Script for converting AIMAll output to XML .top format.

mgpviz2top.pl filename.mgpviz > filename.top

The input file must be an .mgpviz file, but the script will also check for the presence of other types of .viz file.
Files containing interatomic surface data (iasviz) are produced by running AIMAll with the -iaswrite=true flag. 
Files with basin visualization data (basviz) can be generated from within the AIMStudio GUI; to the best of our knowledge this cannot currently be done at the command line.
There are two ways to map the gradient paths of an atomic basin to 3D objects.
They can be treated as a set of gradient paths and individually drawn with a curve, or treated as a single mesh and drawn as such.
Rhorix reads basins as sets of gradient paths, and triangulation can be performed internally if requested.
The former is significantly more computationally expensive than the latter.
AIMAll does not appear to put triangulation data in viz files, therefore AIMAll's atomic surface data (interatomic surfaces and envelopes) can only be rendered in Rhorix as a set of gradient paths or points.
Rhorix is able to attempt to triangulate the interatomic surface point data in the AIMAll viz file.
This is performed in Mapping.py of the Python code and currently only functions partially.
The resulting triangulation can not be displayed as a filled-in surface, only a wireframe.
Parsing iasviz isodensity envelope data is not currently supported and the program will issue a warning to make this clear.

### Morphy/Iris Conversion

The following scripts are for running the IRIS program and collecting its output into a single file (mif) respectively, then converting to XML .top format.
The mif file does not contain any atomic basin data, so these cannot be visualized with IRIS.
There are certain other limitations of the mif file, in particular the full connectivity of the molecular graph is not written and must be inferred from distances between gradient path points and critical points.
These files also do not clearly differentiate between envelopes and interatomic surfaces, and contain triangulations thereof only (not individual gradient paths).
Iris is currently the only program that produces triangulated surfaces for Rhorix.

mif2top.pl - Script for converting MORPHY/IRIS output to top format.

mif2top.pl filename.mif > filename.top

runIris.pl - Run the various executables that comprise IRIS on a set of wavefunctions.

collateMifs.pl - Collect the various mif files produced by IRIS into a single file for conversion.

### General
centerTop.pl - Move a topology so that its origin is at the center of mass of its nuclei.

This is useful when a topology loaded into Blender is too far from the view center to be easily manipulated.
Please note this script relies on x,y and z tags not being broken over multiple lines.

validateXML.pl

This is a simple script that verifies that a given XML file conforms to its listed document type definition.
It should be used to check any .top file produced by these conversion scripts.

## General Use Modules

In the following, *italics* indicate that a subroutine is made public by its parent module and thus may appear in an above script.

### Utilities
Contains generic utility functions related to reading/writing files and dealing with arguments.

*stripExt* - Remove the extension from a filename.

*getExt* - Get the extension from a filename.

*readFile* - Open and read the contents of a file.

*checkArgs* - Check that the appropriate arguments have been passed to a script.

*listFilesOfType* - Make a list of all files with a given extension in a directory.

### XmlRoutines
Contains routines expressly dedicated to writing to XML files and checking their validity against a document type definition.

*writePCData* - Write a parsed character data XML element.

*openTag* - Write an XML element open tag.

*closeTag* - Write an XML element close tag.

*writeXMLHeader* - Write the header of an XML file.

*checkValidity* - Check an XML file against its specified DTD file.

### WriteTopology
Contains routines for writing files which adhere to the topology document type definition.

*writeTopologyXML* - Write a complete topology file.

writeSourceInformation - Write a complete source information element.

writeNuclei - Write a set of nuclei.

writeNucleus - Write a single Nucleus.

writeCriticalPoints - Write a set of critical points.

writeCP - Write a single critical point.

writeGradientVectorField - Write a complete gradient vector field element.

writeMolecularGraph - Write a complete molecular graph element.

writeAtomicSurfaces - Write a set of atomic surfaces.

writeAtomicSurface - Write a single atomic surface.

writeInteratomicSurface - Write a single interatomic surface.

writeEnvelopes - Write a set of constant electron density envelopes.

writeEnvelope - Write a single constant electron density envelope.

writeAtomicBasins - Write a set of atomic basin elements.

writeAtomicBasin - Write a single atomic basin element.

writeRingSurfaces - Write a set of ring surface elements.

writeRingSurface - Write a single ring surface element.

writeRing - Write a ring element.

writeCage - Write a cage element.

writeTriangulation - Write a triangulation element.

writeEdge - Write an edge element.

writeFace - Write a face element.

writeAtomicInteractionLine - Write an atomic interaction line element.

writeGradientPaths - Write a set of gradient path elements.

writeGradientPath - Write a single gradient path element.

writePoint - Write a single point element.

writePositionVector - Write a single position vector element.

writeMap - Write a single map element.

writePair - Write a single pair element.

### TopUtils

*getRank* - Convert a critical point label to the corresponding integer rank value.

*getSignature* - Convert a critical point label to the corresponding integer signature value.

*computeCOM* - Compute the center of mass of an array of nuclei.

*getMassesFromElements* - Convert a list of element labels to their corresponding masses.

getMassFromElement - Convert a single element label to the corresponding mass.

countNACPs - Given a list of CPs, count the NACPs.

findClosestCPToPoint - Find the closest of a set of CPs to a given test point.

distance - Compute the distance (Euclidean norm).

## Topology Program Specific Modules

### ParseViz
Contains functions for reading from AIMAll's .*viz formats and creating corresponding objects.

*parseMgpviz* - Master routine for parsing contents of an .mgpviz file.

The remainder of the subroutines in this module have obvious function given their names.

parseRingSurfacesFromMgpviz

parseInteratomicSurfacesFromMgpviz

parseSourceInformationFromViz

parseNucleiFromViz

parseCPsFromViz

parseMolecularGraphFromViz

parseGradientPath

parseRelatedIasvizFiles

parseRingSurfacesFromIasviz

parseBasinFromBasviz

parseAtomFromIasviz

parseAtomicSurfaceFromIasviz

parseIntegrationRayIsodensitySurfaceIntersectionsFromIasviz

determineRings

determineCages

### VizUtils
Contains basic utilities related to AIMAll's .*viz file formats.

*checkMgpvizFile* - Confirm that an .mgpviz file is complete and correct.

checkPoincareHopf - Check that a .viz file does not violate the Poincare-Hopf relationship.

checkCompletion - Check for the presence of a completion statement in a .viz file.

