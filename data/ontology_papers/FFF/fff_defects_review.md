International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 https://doi.org/10.1007/s12008-022-01026-5 

**ORIGINAL PAPER** 



# **Fused filament fabrication: A state-of-the-art review of the technology, materials, properties and defects** 

#### **Aniket Yadav**<sup>**1**</sup> **· Piyush Rohru**<sup>**1**</sup> **· Atul Babbar**<sup>**2,5**</sup> **· Ranvijay Kumar**<sup>**1,3**</sup> **· Nishant Ranjan**<sup>**1,3**</sup> **· Jasgurpreet Singh Chohan**<sup>**1**</sup> **· Raman Kumar**<sup>**1**</sup> **· Manish Gupta**<sup>**4**</sup> 

Received: 28 May 2022 / Accepted: 9 August 2022 / Published online: 24 August 2022 © The Author(s), under exclusive licence to Springer-Verlag France SAS, part of Springer Nature 2022 

#### **Abstract** 

Fused filament fabrication (FFF) is one of the additive manufacturing (AM) techniques that have revolutionized the manufacturing strategy in the last 2 to 3 decades. The quality of the parts prepared by the FFF process is dependent upon the static and variable process parameters. It has been reported by previous studies that part shrinkage, part shrinkage, high surface roughness, warping from the edges, misaligned part geometry, lack and loss of the adhesion, part distortion, voids and porosity etc., are the major issues in the fused filament fabrication process. In the case of open-source fused filament fabrication, internal and external factors such as; the variable room temperatures, room humidity, wind speed, heterogeneity in feedstock materials, torsion in feedstock filaments, vibration due to any source, nozzle clogging, nozzle choking, high/low nozzle and bed temperature are conducive for the mentioned issues. The present study is the state of review for minimizing defects in the final product by suggesting the methods and procedure for each issue in the FFF process. This study would be helpful for novice researchers who are working on different applications of the FFF process. In this review work, most common defects and problems observed during 3D printing are elaborated and discussed according to literature review and also solution of defects has been discussed. 

**Keywords** FFF · Materials issues · Warping · Low adhesion · Defects in FFF · Reinforcement · Additive manufacturing · 3D Printing 

## **1 Introduction** 

At present, machining and AM are the two major processes, which are used to make a product or prototype. The accuracy of machining is good but it is difficult to make complex structures and intricate dimensions. In comparison, 

- Atul Babbar atulbabbar123@gmail.com 

- 1 Department of Mechanical Engineering, Chandigarh University, Mohali, Punjab, India 

- 2 Department of Mechanical Engineering, SGT university, 122505 Gurugram, Haryana, India 

- 3 University Centre for Research and Development, Chandigarh University, Mohali, Punjab, India 

- 4 Division of Research and Development, Lovely Professional University, Phagwara, India 

- 5 Shree Guru Gobind Singh Tricentenary University, 122505 Gurugrma, Haryana, India 

AM can produce complex structures [1]. AM is a process to fabricate a Three-Dimensional (3D) model through deposition of required material layer by layer according to the inserted computer-aided design (CAD) design [2]. 3D printing is also known as rapid prototyping, which makes the component with good accuracy, joint less and with higher strength [3]. In AM, a very less amount of wastage is there [4]. 3D printing is mostly used to make complex structures like dental implants [5] and dies [6] etc. This technology is used in almost every field like biomedical industry [7], aerospace industry [8], automobile industry [9] and teaching [10]. There are many types of 3D printing like fused deposition modelling (FDM) [11], Stereolithography (SLA) [12], digital light processing (DLP) [13], selective laser sintering (SLS) [14], selective laser melting (SLM) [15], laminated object manufacturing (LOM) [16], and electronic beam melting (EBM) [17]. Out of these techniques, FDM is most common due to its less cost and acceptable surface finish [18]. The founder of the FDM is Scott Crump, Minnesota in the USA [19] and the standard name of this is 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2868 



<!-- Start of picture text -->
Extrusion Head<br>Extrusion Nozzle hy<br>Support Materials, a Fabricated Part<br>Foundation Say ~_— t t<br>sheet igs<br>Build Platform i<br>Support Material<br>spool f<br>Printing Material<br>spool<br><!-- End of picture text -->

**Fig. 1** Schematic of FDM with part and support material 

material extrusion additive manufacturing (MEAM) [20]. In this technique a filament wire is used with an approximate thickness of 1.75 mm [21], this filament wire is heated and extruded out through the nozzle and deposited on the heat bed. As nozzle moves in X & Y plane and the bed moves in the Z direction so that the semi-liquid filament is deposited on the heat to form one layer of the specimen. 

When one layer is extruded, it makes the bond with the other layer and solidifies [22]. In these 3D printers, a heated bed is used so that when the semi-liquid filament deposit on the bed it will stay heated to make a bond with the next layer [23]. Also, a second nozzle is used for the support material to fabricate a part like a sphere, cantilever beam and any structure which needed support. Figure 1 shows the process and support material can be removed after the part is completed [24]. 

In FDM, there are variable parameters like nozzle speed, nozzle temperature, infill pattern, infill density, orientation angle, layer thickness and bed temperature that can affect the strength and accuracy of the fabricated component [25]. These variable parameters help to change the final properties of the component in the form of flexural strength, compressive strength [26] and tensile strength [27]. FDM uses the materials like acrylonitrile butadiene styrene (ABS) [28], polylactic acid (PLA) [29], polyamide [30], polycarbonate (PC), high-density polyethylene (HDPE), and polyurethane (PU) [31]. However, out of those materials, ABS and PLA are mostly used due to their easy availability, cheap cost, non-toxicity, flexibility, uniformity and fast printing. This technique is used to fabricate parts in small batches, so the parts or components should have high accuracy and a high surface finish. However, the accuracy, strength and surface 

finish of FDM components is not very good [32]. In addition, the shrinkage is equal from every side [33]. One of the major problems in FDM is warping. When the feedstock filament is extruded out then the dimensions of the printed component is decreased as each layer cools at a different time [34]. After fabricating a component through FDM then there is a need for machining e.g. if support is provided to the component then support material should be removed after completing the component. Also, to remove the sharp edges of the fabricated part, some machining is required [35]. Table 1 shows the configuration of commercial FFF 3D printers. 

Based on Table 1 it has been observed that, FFF are present in different size and also for different applications according to their needs and requirements. According to Table 1 it helps to select the 3D printer based on materials to be used and size of the final manufactured parts. 

### **1.1 Research work and gaps** 

The previous studies have highlighted the tools, techniques, processes and methods for FFF of plastics, metals and their composites for extraordinary practical and prototyping applications. Some of the studies have highlighted the critical issues regarding the fabrication and material issues for the production of high strength components by the FFF process. Hitherto, few studies have been reported that delivers the suggestion in form of tools, process and method to reduce the component defects and maximize the sustainability of products. The present study is the state of review for minimizing defects in the final product by suggesting the methods and procedure for each issue in the FFF process. This study would be helpful for novice researchers who are working on different applications of the FFF process. Figure 2 shows the bibliographic analysis of previous studies using the web of science database. By putting the keyword ‘fused filament fabrication, a total of 1284 research papers have been reported from 1999 to 2021 and the first 500 has been selected for the bibliographic analysis by the Vosviewer software package. A total of 12383 terms have been found and among those 279 terms have been met the threshold taking a minimum number of occurrences of 10. Among 279 terms, the most relevant terms have been selected for analysis as shown in Fig. 2. 

The analysis has suggested that there is several investigations have been reported for resolving the issues in FFF related to the effect of layer height, orientation, speed, printability, dimensional printing, process parameters, layer thickness, nozzle temperature, reinforcement, thermal stability, etc. 

Figure 3 shows the bibliographic representation of previous studies of FFF about investigations of printability. The 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2869 

|**Table 1**Common FFFprinter configurations||||||
|---|---|---|---|---|---|
|i<br>Manufacturer/ Printer types|Feedstock<br>materials|Filament size|Build size|Post-process<br>requirements|Ref.|
|LulzBot TAZ 4 3D Printer/Cartesian|ABS|1.75 mm|297×274×249 mm|Side edges removal|[36]|
|Rostock MAX V2.0/Delta|PLA|3 mm|197×197×375 mm|milling|[37]|
|TAZ 4 FFF printer/Cartesian|ABS|2.85 mm|280×280×285 mm|annealing|[38]|
|Creator pro/Cartesian|PLA|1.75 mm|225×145×150 mm|Annealing|[39]|
|LulzBot TAZ6 3D Printer/Cartesian|ABS|1.75 mm|280×280×250 mm|Cellulose nanocrys-<br>tals+Water+Air<br>mixture|[40]|
|MakerBot Replicator 2X Experimental 3D<br>Printer/Cartesian|PCL|1.75±0.15 mm|246×152×155 mm||[41]|
|uPrint SE/Cartesian|ABS-P400|1.75 mm|203×152×152 mm|Chemical Vapour<br>smoothing|[42]|
|Makerbot Replicator 2/Cartesian|PLA, PEG<br>400,DEP, Gelatine<br>capsules,RF5’P<br>Na|1.75 mm|246×152×155 mm|Annealing|[43]|
|Craftbot Plus/Cartesian|HPMC,EPO,<br>HPC,PVA|1.65±0.1 mm|250×200×200 mm|Post-hot metal<br>extrusion|[44]|
|Delta WASP 20 40 printer/Cartesian|ABS|1.75 mm|200×200×400 mm|finishing|[45]|
|uPrint-SE/Cartesian|ABS|1.75 mm|203×152×152 mm|i<br>Chemical Vapour<br>smoothing|[46]|
|Hyrel 3D/Cartesian|ABS|1.75 mm|400×300×250 mm|Finishing with<br>Acetone and methyl<br>ethyl ketone (MEK)|[47]|
|Fortus 400 mc 3D printer/Cartesian|ABS, PLA, PEI|1.75 mm|355×254×254 mm|<br>Edges removal|[48]|
|Ultimaker 2 Extended+/Cartesian|CRF-Nylon|2.85 mm|228×226×304 mm||[49]|
|Fortus 400mc machine/Cartesian|ABS|1.75 mm|355×254×254 mm|Grinding|[50]|
|MakerBot Replicator 2X Desktop/Cartesian|Kollidon VA 64,<br>PEG 1500, man-<br>nitol, ramipril<br>and magnesium<br>carbonate|1.3 mm|250×160×150 mm||[51]|
|Dimension Elite 3D Printer/Cartesian|ABS-P430,<br>P400SR|1.75 mm|203×203×305 mm|Removal of support<br>material from work<br>piece|[52]|
|RapMan 3.0 open-source/Cartesian|ABS|1.75 mm|220×220×250 mm|Thermal treatment<br>i|[53]|
|Mr300 3D printer/Cartesian|PLA, PCL and<br>POE|1.75 mm|300×300×300 mm|Chemical finishing|[54]|
|Objet500 Connex; Stratasys, Ltd/Cartesian|Multimaterials|1.75 mm|490×390×200 mm|Not Done|[55]|
|RepRap 3D printer/Delta|PLA|1.75 mm|260×260×435 mm|Not Done|[56]|
|ORION Delta 3D manufactured by<br>SeeMeCNC/Delta|High impact poly-<br>styrene (HIPS)|1.75 mm|150×106×235 mm|Not Done|[57]|
|RepRap/DElta|PLA and Waste<br>Wood|1.75 mm|260×260×435 mm|Finishing.|[58]|
|Kossel mini/ Delta|ABS|1.75 mm|167×167×238 mm|Removal of support<br>material|[59]|
|Delta|ABS, PLA and Cu|1.75 mm|260×260×435 mm|Chemically using<br>acetone vapour or<br>bath|[38]|
|Osals Polar/ Polar|PLA|3 mm|1800×1800×1500 mm|Not Done|[60]|
|Replicator 2/ Polar|PLA|1.75 mm|284×152×152 mm|Not Done|[61]|
|<br>3D Cloner DH/Cartesian|PLA|1.75 mm|280×197×375 mm|3D Cloner requires|[62]|
|And Rostock Max V2/ Delta|||(Rostock Max V2) And<br>320×220×410 mm(3D<br>Cloner DH)|<br> <br>post processing for<br>enhancing finishing||
|Felix Pro 3/ Cartesian|PLA|1.75 mm|430×390×550 mm|Finishing|[63]|
|Orcabot XXL / Cartesian|PLA|1.75 mm|360×280×230 mm|Not Done|[64]|



1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2870 



<!-- Start of picture text -->
ego elastic qoduius yp,<br>i eat ZS<br>wg tenses 7) oa aI — thermalgeabilty<br>Po nanocaipposite ie \<br>Lt sere = dimensio(igl printing 7<br>nozzle temperature aoe cgplanshape Sy,<br>process (parameter Irigiig “<br>layer thlekness<br>Ac vosviewer<br><!-- End of picture text -->

**Fig. 2** Bibliographic map analysis for reported studies of the FFF process (data source: www.webofknowledge.com) (colour of nodes represent the clusters) 

relation to solving the printability issues, previous studies have been reported for the investigation’s thermal stability, formation of complex shapes, dimensional printing, layer thickness, printing speed, orientation, strain, elongation, elastic modulus etc. Future studies may be conducted for the investigation of solving printability issues in terms of 

nozzle diameter, nozzle temperature, printing parameters, sintering, reinforcement, printing temperature, bed temperature and etc. 

Due to this research study, it has been observed that which areas are most highlighted and mostly worked in 



<!-- Start of picture text -->
carb@fiber elong@tion__5 elastic@eduWyi tabilty<br>a. N<br>SS nano posite \ I”<br>. t ‘ —F<br>‘<br>Ss dip. E/* dimensiog| printing<br>parar<br>—<br>layer (@igkness<br><!-- End of picture text -->

**Fig. 3** Bibliographic gap printability in FFF process (colour of nodes represent clusters) 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2871 



<!-- Start of picture text -->
FILAMENTPIE  WIRE oe<br>NOZZLEMOVEMENTWITH OFTHE XANDY-<br>ax<br>MOTORS<br>PRINT BED WITH.<br>"THE MOVEMENT<br>OFZAXIS<br><!-- End of picture text -->

**Fig. 4** Cartesian FFF 3D printer 

previous years and which areas are less focused that suggest that the research work area. 

## **2 FFF 3D printers** 

### **2.1 Cartesian FFF 3D printer** 

These 3D printers move in X, Y and Z-axis. There are two major subsystems, one is a print bed and the other is an extruder. Print bed moves in Z-axis, it can move in two directions which are denoted as –Z and + Z. Extruder moves in X and Y-axis which moves in 4 directions and is denoted as –X, +X, -Y and + Y [65] (see Fig. 4). Most usable printers based on usability, easy to handle and better output are Ultimaker, Makerbot and Prusa i3. Velez et al. have used the Koala 3D printer and this printer is a combination of a climbing robot with a 3D printer [66]. In this printer, to fabricate a product first printing is done and then it is shifted to the new station and then again printing. Asif et al. have used the Cartesian 3D printers with two extra rotational motions in the nozzle [67]. The combination of ultraviolet-based 3D printing and FDM is used in this research. To fill the material viscosity fumed silica is used as filler. To investigate the effect of photopolymer mechanical tests were conducted with the different concentrations of filler. 

### **2.2 Delta 3D printers** 

Delta 3D printers are one of the most popular printers in terms of usage. These printers are working with the Cartesian plane. But in these printers, circular print beds has remained constant and three arms are holding the extruder over the print bed in a triangular configuration, that’s why it is named Delta [68] (see Fig. 5). Delta 3D printers have good printing speed but the accuracy of these printers is not good as Cartesian printers [69]. Yuan et al. studied the cabledriven parallel robot (CDPR) and focused on the dynamic stiffness and static stiffness [70]. In this research work, prototypes were fabricated using the six degrees of freedom 



<!-- Start of picture text -->
FEEDSTOCKWIRE FILAMENT<br>MOVABLE ARMS OF THE<br>EXTRUDER ——<br>NOZZLE<br>PILLARS OF<br>‘THE PRINTER<br>FIXED PRINT<br>BED<br><!-- End of picture text -->

**Fig. 5** Delta FFF 3D printer 



<!-- Start of picture text -->
‘VERTICAL Z-AXIS<br>BUILD PLATE<br>ROTATION<br>EXTRUDER WITH<br><!-- End of picture text -->

**Fig. 6** Polar 3D Printer 

cable-suspended robot. Effect of static stiffness is calculated by end effectors pose and dynamic stiffness is evaluated by the natural frequency of the robot. Alikhani et al. have used the cable-based parallel robot with three degrees of freedom [71]. In this work, tensional workspace is investigated and the mechanism of tension-ability is proved. 

### **2.3 Polar FFF 3D printer** 

The X, Y and Z coordinates do not define polar 3D printers. It is defined by the angle and length of the object. In this printer, instead of moving in the Z direction, the print bed is rotating and at the same time beds moves according to the length and the extruder moves up and down only. With this rotation and movement of the print bed and extruder, the filament wire is deposited on the print bed [72]. For long work, polar 3D printers are known for their good efficiency and these printers can fabricate a larger object in less space [73]. Figure 6 shows the schematic of the polar FFF 3D printer. 

### **2.4 Scara (robotic arm) FFF 3D printer** 

From small-scale industries to large-scale industries, robotic arms are most commonly used for assembly. Automotive 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2872 



**Fig. 7** Robotic Arm 3D Printer 



**Fig. 8** Effect of colder room temperature on ABS material 

industries are based upon robotic arms. 3D printing also uses robotic arms in production like in building and bridges manufacturing but robotic arms are in the developing stage [74]. The selective compliance assembly robotic arm (SCARA) is the most used robot and it is a very precise system with good efficiency [75]. Figure 7 shows the schematics of SCARA FFF 3D printers. 

In this printer, the print bed is heated and remain fixed. The extruder is attached to the robotic arm, it can move in all directions with three degrees of freedom, first is for horizontal movement and second is for vertical movement, and the third one is for the movement of the extruder [76]. 

## **3 Issues due to an uncontrolled environment** 

### **3.1 Room temperature** 

In 3D printing, room temperature can affect the quality of the printed object. Before printing any material, conditions of the room should be in mind [77] e.g., PLA material can be printed at cold room temperature (15℃ to 25℃) [78] and for some materials like ABS and PETG, warmer room 



**Fig. 9** Adhesion problem with bed due to uncontrolled room humidity 

temperature is required [79]. Figure 8 show the part prepared under uncontrolled room temperature. These materials are suitable for 25℃ to 30℃ room temperature. The lower room temperature can affect the accuracy and efficiency of the printer [80]. Also colder or warmer room temperature can affect the heat bed and extruder to reach their assigned temperature. They usually take more time to heat up in cold room temperature and warm room; it can take less time than actual [81]. If the printer is insulated then room temperature will not affect printing. 

### **3.2 Room humidity** 

Mostly, the filament materials are hygroscopic, which is tending to absorb the moisture from the air [82]. After certain hrs. in a humid room, filament material start to swell [83] and indications of the moisture contents in the material are like filament cracks [84], due to moisture, small bubbles can be seen at the extruder tip [85], material slips from extruder motor [86], adhesion problem with the bed [87] and error in the accuracy of the printed object [88]. Whereas, Fig. 9 shows the part defect caused by uncontrolled room humidity. 

Increased fragility, increased diameter (potential issues with printers using a Bowden-type extrusion mechanism), filament degradation, breaking filament, etc. are all issues that can result from attracting water. Additionally, it is important to remember that the extrusion temperature will be higher for the filaments that have absorbed water. If you aren’t going to print, remember to keep the filaments out of the printer. Because they gain weight and grow in diameter when they absorb water, they might become trapped in the extruder. At 200 °C or more within the extruder, the water inside the filament is heated and rapidly boils, resulting in bubbles, pops, or other undesired results. Humidity 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2873 

might cause filaments to swell, which could be problematic because it could increase friction between the throat’s walls and the hot end, leading to under extrusion. You can either pre-heat the filament at 50 °C sufficient or have it pass through a little sponge before entering the hot end to avoid moisture from the filament surface from entering the hot end. Although ABS is more resistant to moisture, it stinks when printed. Although PLA is non-toxic, it is more sensitive to dampness. Direct contact with water won’t erode PLA, however, soluble colourants will cause small holes to form. 

We can see the difference between the newly opened filament material and the old filament material. The object which is printed by an old filament will be softer, have less inter-layer adhesion [89] and have low accuracy. To overcome the problem of room humidity, there are some filament cabinets available that will heat the environment when needed [90]. But there are some demerits too with this cabinet after 6 h of heat material like ABS can do a chemical reaction with environmental gases. 

### **3.3 Wind speed** 

For perfect efficiency and accuracy of 3D printer wind speed in the room should be negligible [91], with high wind speed 3D printer cannot perform with good accuracy [92]. PLA, ABS, PETG and other 3D printing filament materials have the property of rapid cooling extruded out from the nozzle of the extruder and the heat bed is kept hot to the material up to their glass transition temperature [93]. At this time, if the wind speed is high in the room, it will cool the material before being deposited on the previous layer of the print and due to this interlayer adhesion will be weak [94]. Because of weak interlayer adhesion; there will be less strength, poor surface finish and less dimensional accuracy. If the printer is insulated then these factors cannot affect the print and quality will remain the same [95]. 

## **4 Material issues** 

### **4.1 Virgin thermoplastic** 

It is a type of plastic polymer that can be mouldable in any shape at a particular temperature and after heating, it solidifies [96]. There are many techniques to give shapes to polymer-like injection moulding [97], extrusion [98] compression moulding [99] etc. There are many types of thermoplastic polymer like ABS, PLA, Nylon, PE, Teflon, PP, Polystyrene etc. [100]. These different-different polymers have different-different properties like melting point, glass transition temperature and strength [101]. If these filaments 

plastics are heated repeatedly then there may be some defects in the form of voids, cracks and porosity. These defects can cause an error in the final printed object and especially these defects cannot be seen from outside [102]. So it is always recommended not to reheat plastics many times specifically in the case of 3D printer feedstock filament. 

### **4.2 Polymer matrix composites** 

Polymer Matrix composites are composite materials with the combination of multi-phase material in which reinforcement of any other material, according to the requirement of composites [103]. This reinforcement will change their mechanical properties, which cannot be gained from a single component [104]. In 3D printing, reinforcement can be done in any form e.g., a spray of any other material [105], some reinforced filament with a combination of materials can be made using extrusion process [106] and directly sticks a layer of different material on feedstock filament wire [107]. In all these techniques, reinforcement through spray is most easy. There can be two ways to spray, the first one is with nozzle spray, which is attached to the printer, and another one is to spray manually [108]. But there is a problem in a manual spray like the density of spray on each section of the object cannot be the same and it spills here and there due to little movement of hands. 

### **4.3 Ceramic and clays** 

Ceramic materials are highly known for their brittleness, hardness, high melting point, strong compression strength and weak shearing and tension strength [109]. This material is used in almost every industry like chemical industry [110], biomedical industry [111], electronics [112] and aerospace industry [113]. Through 3D printing, any shape of ceramic material can be achieved with or without using binders. After preparing the power ceramic or clay and depositing a layer according to CAD design it takes time to solidify as this is not a polymer [114]. Holes or spherical bodies are difficult to make in ceramic material because support material is rarely used. After the printed object solidifies, it becomes harder, so machining the printed object is very difficult if required in any case. Due to friction of tool, printed object be broken [115]. In addition, it is difficult to achieve a good surface finish in ceramic material printing. 

### **4.4 Metals** 

As 3D printing is associated with rapid prototyping creating metal prototypes of intricate designs using conventional techniques is a tough and time-consuming job [116]. To reduce this time and other complexities 3d printer can be 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2874 

used for printing metals. Mainly the metal used in metal 3D printing is aluminium, stainless steel and titanium [117]. It allows for the fasted fabrication of objects by using metal filament instead of polymer filament [118]. Metal 3D printers can only fabricate limited parts in a day. It has some issues with porosity, surface finish, part shrinkage and density [119]. When the material is heated then there are some bubbles and voids in the part. Also, post-processing is required in some cases to give a better surface finish [120]. There is a need to take a little allowance in some cases due to the shrinkage of metal [121]. 

### **4.5 Food materials** 

3D food printing is a variety of AM, which helps to make a food product. Instead of an extruder in an FDM printer [122], a food-grade syringe in which food material will be inserted and printed on the print bed according to the CAD design by food grade nozzle [123]. Chocolate in food printing is the main material, which is melted first and then extruded out from the nozzle on the print bed [124]. Soft material past can be directly printed like cheese, jelly and mashed potato [125]. In this extrusion-based food printing sugar, protein etc. are mixed up with food material to give a good viscosity [126]. The main issue with food printing is the viscosity of the material, if the proper viscosity is not there then the layers will not be stick with each other and a product cannot be fabricated [127]. Also, this technique takes a long time to fabricate a single product. 

### **4.6 Biological materials** 

3D bioprinting is mainly used to print the human organs and ligaments like teeth, knee joints hip joints etc. [128]. As every human body part have a different shape and properties e.g., teeth, so a 3D scanner is also required to scan the part first and then give commands accordingly to the printer [129]. Biomaterials have properties like hydrogels either it is too thick or too thin after reaching their melting point [130]. So, after reaching the melting point it is very difficult to control the movement on the bed [131] and in scaffolds, very high accuracy is needed as a small error cannot be negligible for the human body [132]. Post-processing is also required in bioprinting for good finishing and to remove the sharp edges [133]. Also, to make the materials proper viscous binders and fillers are used. Table 2 shows the summary of common materials their effect on printing quality. 

## **5 Feedstock filament issues** 

### **5.1 Diameter of feedstock filaments** 

Feedstock filament wires are generally used for fused deposition modelling 3D printing [158]. These filament wires are available with different materials and different properties. Common materials in FDM are ABS, PLA, Nylon PETG etc., these materials have different melting points and glass transition temperatures [159]. The standard size for FDM printers is 1.75mm and 2.85mm [160]. In 3D printing sometimes, there is confusion between nozzle diameter and filament diameter, nozzle diameter is from 0.1mm to 0.5mm [161]. In feedstock filament sometimes, there are variations in the diameter of the filament. If a filament is made with 1.75mm or 2.85mm then there can be shrinkage and swelling of materials due to heat or cold environment temperature [162] and due to this environment change size of the filament will be uneven from everywhere which will cause defects in the printing [163]. 

### **5.2 Voids and porosity in feedstock filaments** 

Voids and porosity are because of the poor manufacturing of the material for the feedstock filament [164]. Voids can be the reason for the cracking when a small load is applied to the filament [165] (see Fig. 10). Voids and porosity affect the properties of the material like compressive strength and tensile strength [166]. These are the pores, which remains unfilled during the manufacturing. The reason for the voids and porosity formation can be very low and high temperature while extrusion, proper escape of gases might not occur during heating [167]. These voids and porosity issues in the feedstock filament will cause defects in dimensional accuracy and surface finish of the printed parts and voids will be still there in the final printed part [168]. In some industries, very a much smaller number of voids are acceptable e.g., aerospace industries (< 1%) as in this industry very high accuracy is required [169]. 

### **5.3 Overheated/semi-burnt feedstock filaments** 

3D printing filaments are created by the heating of required material and extruded out through the extruder in the form of wires [170]. In this extrusion, process the rollers instead of pushing [171] to pull heated material. Overheated and semi-burnt feedstock filament is produced when extrusion temperature is much higher than its glass transition temperature [172]. The standard temperature for polymers while extrusion is 80℃ to 110℃ e.g., ABS and PLA [173]. This overheating of the filament makes it hard and brittle than its actual form and this overheating change the material 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2875 

**Table 2** Materials and their effect on printing quality 

|S.<br>No.|Material type|Type of<br>printing|Effect|Application|Remarks|Ref.|
|---|---|---|---|---|---|---|
|1|Thermoplastic|Fused<br>filament<br>fabrication|Porosity,<br>Void and fibre volume<br>fraction,<br>Length and orientation|Medicine,<br>Automotive,|The importance of fibre flow and void<br>formation during 3D printing has been<br>highlighted.|[134]|
|2|Thermoplastic|Fused<br>filament<br>fabrication|Stress,<br>Strain,<br>Flexural strength,<br>Hardness,<br>Weight loss|Aerospace,<br>Automotive,<br>Medical|Samples with higher thermal tolerance,<br>higher strength, and superior hardness<br>were successfully fabricated.|[135]|
|3|Thermoplastic|Fused<br>filament<br>fabrication|Layer height,<br>Stress,<br>Strain,<br>Orientation<br>l|Orthopaedic,<br>Aerospace|The variable gravity load during FFF<br>affects the cooling behaviour, inter-layer<br>adhesion, and distribution of material<br>phases.<br>f|[136]|
|4|Composites|Fused<br>filament<br>fabrication|Heat flow,<br>Weight%<br>Tensile stress<br>Strength,<br>Proliferation|Orthopaedic,<br>Tissue engineering|The scaffolds with enhanced mechani-<br>cal and biological properties have been<br>successfully prepared using PLA and<br>titanium.|[137]|
|5|Composites|Fused<br>filament<br>fabrication|Heat flow,<br>Weight loss, Relative<br>permittivity,|Radiofrequency<br>devices, satellite and<br>telecommunication|Zone plate lens has been fabricated<br>using the composite functionally graded<br>material.<br>i  i|[138]|
|6|Composites|Fused<br>filament<br>fabrication,<br>Laser-<br>based<br>powder<br>bed fusion|<br>Tensile strength,<br>Shear strength|Composite<br>components,<br>Drug delivery devices|Significant polymer infiltration has been<br>observed in mechanical structures.|[139]|
|7|Ceramic|Powder<br>bed 3D<br>printing|Intrinsic porosity, Densifica-<br>tion, Mechanical<br>Strength,<br>Compressive stress|Bone scaffolds<br>Load-bearing|Higher nozzle temperature resulted in<br>enhanced strength and density.<br>Nanopowder granules caused better<br>control of the porosity with high strength<br>interconnected macrospores.|[140]|
|8|Ceramic|Fused<br>filament<br>fabrication|Viscosity,<br>Green filament density,<br>Microhardness,<br>Roughness|Bone replacement,|The composite with 7.75 vol% Si3N4<br>(HAp10SN) showed enhanced osseoin-<br>tegration, better bioactivity and exhib-<br>ited as a potential candidate for bone<br>replacement.|[141]|
|9|Clay (blends)|Fused<br>filament<br>fabrication|Surface roughness,<br>Stress, Young’s modulus|Respiratory devices,<br>Infusion systems|The blend is prepared with ABS and TPU<br>in 10-20wt% TPU and 30wt%TPU caused<br>good adhesion of successive layers with-<br>out affecting yield strength.|[142]|
|10|Metals|Fused<br>filament<br>fabrication|Shear strength,<br>Tensile strength,<br>Surface morphology|Orthopaedic,<br>Prosthetic,<br>Implants|f<br>The joining strength has been significantly<br>increased with laser heating during the<br>joining of copper, stainless steel, and PLA.|i<br>[139]|
|11|Metals|Fused<br>filament<br>fabrication|Intensity,<br>Extrusion force<br>Heat flow,<br>Strength|Metallic glasses|Little shrinkage and better processability<br>have been observed.|[143]|
|12|Metals|Fused<br>filament<br>fabrication|Viscosity,<br>Pressure drop,<br>Shear force,<br>Strength|Implants,<br>Porous structure,<br>Automotive brake<br>lever.|It has been observed that higher strength<br>in comparison to force leads to efficient<br>MF<sup>3</sup>printing.|[144]|
|13|Food materials|Extrusion<br>based 3D<br>printing|Appearance,<br>Weight,<br>Microstructure,<br>Content|Snack products<br>Dairy products|The results highlighted that fibre rich<br>snacks can be made using a mixture of<br>milk powder and whole grain rye<br>Flour.|[145]|



1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2876 

**Table 2** (continued) 

|S.<br>No.|Material type|Type of<br>printing|Effect|Application|Remarks|Ref.|
|---|---|---|---|---|---|---|
|14|Food materials|Extrusion<br>based 3D<br>printing|Pore size,<br>Fill pattern,<br>Pore fraction,<br>Moisture content,<br>Compressive force|Cubical shaped snacks|Printing path, compressive force, and<br>imbalance are significant characteristics<br>that affect chewiness and hardness.|[146]|
|15|Food materials|Fused<br>filament<br>fabrication|Intensity,<br>Heat flow,<br>Transmittance,<br>Viscosity,<br>Force|Wheat starch,<br>Snack products|Dry heat treatment significantly enhances<br>the properties of hydrogels, thereby, of<br>wheat starch.|[147]|
|16|Bio Materials|Hot Metal<br>Extrusion<br>and Fused<br>Filament<br>fabrication|Alignment of anisotropic<br>particles, biomass|Food, Biomedicine,<br>cosmetics and other<br>chemical industries.|Progress of cellulose, hemicellulose and<br>lignin were investigated as multicompo-<br>nent of bio feedstock.|[148]|
|17|Polyethene<br>Glycol|Screw<br>Based<br>extrusion<br>3D printer|Green density and surface<br>roughness|Heat Sinks and<br>ornaments|To check the voids and porosity in the<br>printed specimens with optimized and<br>non-optimized parameters, Microtomogra-<br>phy scans were used.|[149]|
||Thermoplastic|Fused<br>filament<br>fabrication|The effect of tungsten addi-<br>tive on printer emissions,<br>particle size|small-scale devices<br>across automotive,<br>aerospace, defence,<br>medical, and con-<br>sumer electronics<br>industries|The objects printed with metal additives<br>have a higher rate of particle emission<br>than the objects printed with polymer only.|[150]|
|18|Thermoplastics|Fused<br>filament<br>fabrication|Annular backflow and buck-<br>ling models|Automobile industry|It describes the importance of the shear-<br>thinning regime in 3D printing|[151]|
|19|Nitrogen-doped<br>diamond films.||structural quality<br>and enhancement of<br>photoluminescence|particle detectors,<br>single-photon emitters<br>in quantum informa-<br>tion technology|<br>By using the hot chemical vapour deposi-<br>tion Pure and N doped nanocrystalline<br>diamond films were made<br>fi|[152]|
|20|Thermoplastic|Fused<br>Deposition<br>Modelling|Uniform homogeneity and<br>good dispersion of particles,<br>X-Ray and tomography|radio-frequency<br>heating of magnetic<br>particles|This new Technique avoids the difficulty<br>of multi extrusion outlets and it helps for<br>smooth and continuous filament running.|[153]|
|21|Thermoplastic|Fused<br>Deposition<br>modelling|Physical, mechanical, elec-<br>trical and thermal properties|x-ray<br>radiation-shielding,<br>biosensors|Pure thermoplastic is compared with com-<br>posite thermoplastic and it is found that<br>composite material has good properties<br>than pure thermoplastic.|[154]|
|22|AMP-PEEK|Extrusion<br>Based 3D<br>printer|Thermal, Rheological and<br>Physio-Chemical properties|Bio-medical industry.|<br>It is shown that AMP-PEEK has relevant<br>properties 3D printing and high zero shear<br>property.|[155]|
|23|PEEK|Fused<br>filament<br>fabrication|Surface morphology, extru-<br>sion diameter of extruded<br>diameter, reducing surface<br>defects|Bioengineering,<br>Automobiles and<br>aerospace.|With the use of optimized control<br>algorithm Stability of PEEK material is<br>increased and the surface morphology and<br>accuracy were also increased.|[156]|
|24|Thermoplastic an<br>dielectric constan|d<br>t<br>Fused<br>filament<br>fabrication|Surface morphology and<br>rheology|In electric equipment’s|A dielectric composite was made with low<br>radio frequency and microwave frequency.|<br>[157]|



_*ABS: acrylonitrile-butadiene-styrene; TPU: Thermoplastic polyurethane; HAp: Hydroxyapatite; PLA: Polylactic acid; FFF: Fused filament fabrication; MF_<sup>_3_</sup> : _Metal fused filament fabrication_ 

properties by which they are famous [174]. When these filaments use in FDM printing, it will cause an error in deposition and heating in the extruder and the efficiency and accuracy of the printers is different from actual [175]. 

### **5.4 Torsion in feedstock filaments** 

The extrusion process is used to make a continuous shape after the raw material is melted e.g., filament wires, sheets etc [176]. In this technique, raw material is fed from the top of the extrusion machine (hopper) and a certain force is 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2877 



<!-- Start of picture text -->
POROSITY<br>RACKS,<br><!-- End of picture text -->

**Fig. 10** 3D image with porosity and cracks 

applied to push the melted material so that filament comes out and is pulled by the rollers to make a roll [177]. If more force is applied than the requirement then the material will come outside with faster speed and it will be difficult to change to rollers speed immediately [178]. As the result, the material will bend before reaching rolls and this improper shape or bending is known as torsion in filaments [179]. It will take more space than the straight filaments and is difficult to roll down and these filaments will not enter in the extruder of the 3D printer, so the material cannot be printed on the bed [180]. 

### **5.5 Composition of feedstock filaments** 

A combination of two or more than two materials is known as composites [181] e.g., stainless steel [182] and alloy wheels or cars [183]. Composition is made according to the required properties of the material. Every composite has a different property like melting point and strength etc [184]. ABS plastic is having a composition of acrylonitrile with polybutadiene and polymerizing styrene [185]. Composition in the FDM technique can be done in various ways like with a spray of any other material during printing and mixing with different material in the plastic at the time of extrusion process of filaments [186]. However, sometimes a composite may not prepare according to the requirements as it can vary the melting temperature and is softer or harder than required [187]. Every percentage of different material is important and the percentage should not be if the required material is needed [188]. If the composition is done by spray then there are chances of spilling here and there, also it will not spray with equal density in every portion. 



**Fig. 11** uneven shrinkage of the 3D printed part 

taken for safety especially in the case of metals [190] (see Fig. 11). In FFF 3D printing, some materials shrink more and some materials don’t shrink. The main reason for the shrinkage of plastic is when the temperature is high then due to dehydration of hydrogels [191]. In some industries like the biomedical industry and aerospace industry very much high accuracy is required as even the small deflection cannot be negligible, so materials are also chosen accordingly [192]. There are some disadvantages also with part shrinkage like it can vary the dimensional accuracy due to uneven shrinkage of material [193] and risk of cracking due to shrinkage [194]. Part shrinkage is related to size also like the small part shrink less and the large part shrink more comparatively. 

### **6.2 Part swelling** 

Sometimes a melted layer of 3D printing may swell after being deposited [195]. Most of the FDM printing materials like ABS, PLA and PETG are hygroscopic which is having the property of absorbing atmospheric moisture [196] and when this material heats up then due to moisture a layer may swell than its actual diameter [197]. 

There are many reasons for part swelling in 3D printing like the inadequate temperature of extruder [198], the inadequate temperature of print bed [199] and less layer adhesion with each layer and print bed. Even the swelling of one or two layers can be the reason for bad dimensional accuracy and due to this swelling mechanical properties may change. So, 3D printing is suggested to be done in an insulated chamber for better accuracy and efficiency [200]. Figure 12 shows the swelling in the 3D printed part. 

### **6.3 Surface roughness** 

## **6 Dimensional issues** 

### **6.1 Part shrinkage** 

Generally, most of the plastics and metals shrink after melting and depositing [189], so every time some allowance is 

In 3D printing, surface roughness plays an important role especially in the biomedical industry [201]. FDM is known for their good accuracy but less surface finish. There are various variable parameters in FDM like print speed, nozzle temperature, print bed temperature, infill pattern, infill density and layer thickness [202]. For a good surface finish, it is 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2878 



<!-- Start of picture text -->
part with swelling normal part<br><!-- End of picture text -->

**Fig. 12** part-swelling defects 

necessary to control all these parameters, but in these above parameters layer thickness, infill density and print speed plays a major role (like less the print speed tends to better surface finish and 100% infill density tends to good strength and good surface finish [203]. Less surface finish can also affect the strength and dimensional accuracy [204]. Voids, cracks and extra parts of material on the part which seems not good and sometimes not acceptable for the required work [205]. The bad surface finishes part is not seeming good in 3D rendered morphology and is measured in µm. 

### **7.2 Misalignment of the print bed** 

Misalignment of print bed leads to deformation in the printed product. Misalignment in print bed leads to issues like the improper first layer, leaning prints, weak and deformed infill, layer separation and surface quality [209]. As a result, the desired product will lack in strength, dimensional, accuracy and will be full of many defects. Hence, it becomes very necessary to eliminate the misalignment of print beds to achieve good print quality. For proper alignment of the print bed, it can be set by visual inspection using sprit level or by using electronic sensors. 

## **7 Print bed issues** 

### **7.3 Lack and loss of adhesion** 

### **7.1 Warping issues** 

Warping is one of the common issues that arise in FFF printers and leads to bad dimensional accuracy. As extruder material cools during solidification, it results in a decrease in dimensional accuracy. As all the parts of print cool at variable speed, therefore dimension changes at different speeds [206]. The warping issues may arise due to printing parameters, the design of the product and the material selected for printing. Printing parameters like layer thickness, extruder temperature and infill density are responsible for warping [207]. If we compare ABS, PLA and PETG, then ABS is most sensitive for leading warping issues, due to its high glass transition temperature. For reducing warping in ABS can be mixed with some fabric materials optimum printing settings can be used and sharp corners and large flat areas should be avoided in design, as they are also responsible for warping issues [208]. 

Adhesion is the ability of printing material to stick on the built plate of the FFF printer. Many printers use the bed of stainless steel, glass, PET masking tape etc. However, none of these can work with every type of material [210]. There are also some printing parameters responsible for poor adhesion. For achieving good adhesion check the temperature of the print bed, because some materials need a heated bed for sticking, print speed is also a major cause, fast print speed results in poor adhesion. Also, if the nozzle is too high it will result in bad adhesion. For good adhesion results, some external adhesive agents can also be used. 

### **7.4 Vibration and shock from related source** 

Vibrations in the printer or from some external sources may result in wavy printing patterns and will result in bad dimensional accuracy. There can be mainly two causes for 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2879 

**Table 3** Issues related to adhesion and warping on the print bed in FFF 

|Sr.<br>No.|Issues<br>investigated|Material<br>used|Observations|Ref.|
|---|---|---|---|---|
|1|Adhesion<br>forces|PLA, Nylon,<br>Carbon<br>black,<br>Carbon<br>nanotubes|It was observed that printing temperature, printing<br>speed and bed temperature have a significant effect<br>on adhesion. The best adhesion is found on PLA<br>composites.|[210]|
|2|First printing<br>layer adhesion|PLA and<br>ABS|The best results were achieved at printing the<br>specimens at a temperature slightly above the glass<br>transition temperature.|[212]|
|3|Adhesion<br>f|PLA,<br>PMMA, Cot-<br>ton, Coarse<br>silk and<br>Polyester|PMMA coating on hard PLA before printing resulted<br>in better adhesion between the layers|[213]|
|4|Effect of slicing<br>parameter on<br>adhesion|Thermoplas-<br>tic polyure-<br>thane, PLA,<br>Chlorinated<br>polyethene|Three materials were printed together in combina-<br>tions and it was observed that slicing parameters like<br>infill density and layer thickness have a significant<br>effect on adhesion. It was also found out that printing<br>stiffer material on the first layer will result in better<br>adhesion.|[214]|
|5|Effect of<br>particle size on<br>adhesion<br>f|Polyamide<br>12, zirconia|The size of particles more than 400 μm resulted in<br>a clogged nozzle, which resulted in less mechanical<br>properties due to poor adhesion.|[30]|
|6|Effect of<br>orientation on<br>adhesion|PLA, addi-<br>tive powders<br>(wood,<br>ceramic,<br>carbon,<br>copper and<br>aluminium)|PLA composites made with wood and carbon shave<br>shown very poor adhesion. Printing with an edge<br>orientation resulted in better adhesion.|[29]|
|7|Warping|ABS|It was observed that warping deformation depends<br>on section length. The bigger the length of the sec-<br>tion more will be warping deformation. Splitting<br>section length into segments results in fewer warping<br>deformations.<br>f|[34]|
|8|Warping|PLA|PLA specimens were printed at 12 different tem-<br>peratures and it was found that specimens printed<br>at high nozzle temperature showed fewer warping<br>deformations.|[215]|
|9|Warping|PLA|A real-time data acquisition system was developed to<br>track the warping deformation and to pause the print-<br>ing immediately after detecting warping. The model<br>was tested by printing PLA with a mean accuracy of<br>99.3%.|[216]|
|10|Warping|PLA|Print speed and nozzle temperature were used as input<br>parameters. Minimum warping was noted at 220℃<br>with 15 mm/s speed with 4.55% error. It was also<br>observed that an error of less than 1% can be achieved<br>at 220℃ and 20 mm/s print speed with the application<br>of thermal coated adhesive.|<br> <br> <br>[217]|



vibration in the printer, one is very fast printing speed and another one is mechanical issues [211]. When printing speed is set very fast, when changing orientation in one direction to another direction, it results in some additional force, which acts as shock or vibration in a printer, and affects the print quality. For avoiding these vibrations and shock printing speed should be low. Other reasons can be a loose screw, nut, broken bracket or a spring. Table 3 shows the issues related to adhesion and warping on the print bed in FFF. 

## **8 Extruder issues** 

### **8.1 Extruder idler** 

In the FFF printer idler is used for pushing the filament into the teeth of the drive wheel. Spring or a bush [218] pushes an idler. The idler wheel should not be over tightened, as it will result in damaging the filament and the extruder will be jammed. It can also result in influencing printing results and 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2880 

patchy or uneven print will be obtained [219]. Also, sometimes filament escapes the idler to the side, these results in no extrusion or very bad quality of the print result. For overcoming such issues, modification of drive gear is required. Drive gear should have the proper self-cantering groove. 

### **8.2 Clogging of the nozzle** 

Clogging is one of the major issues in the nozzle. Clogging in extruder nozzle results in increasing the frequency of interruptions in the printing process, which even sometimes requires changing of the nozzle and even to stop the printing process [220]. Many factors may lead to clogging of the nozzle. Nozzle height is a major factor, if there is too much height then the material will get extra time and hence the temperature will decrease and if nozzle height is too much low, the extrusion will not be done properly and the material will tend to go back to the extruder, which will result in the formation of clogs in the nozzle. This clog can result in stopping printing. For avoiding this condition proper room should be maintained in the Z direction. Issues related to clogging can also be sensed at an early stage and stop of printing or improper extrusion can be avoided using some sensors for tracking printing conditions [221]. 

### **8.3 Nozzle choking** 

Choking of nozzle head is one of the major disadvantages of using FFF type 3D printer. Choking of nozzle results in obstruction in material flow and influence the print results or just sometimes there may be no printing at all [222]. The main reason for choking the nozzle is having a material particle size larger than that of the nozzle diameter [223]. By having a larger particle size, it will be stuck at the nozzle head and will result in the choking of the nozzle [224]. There are a few more reasons possible for choking off the nozzle, if the temperature of the lower end of the extruder is low then the material will not flow out properly from the nozzle head and will result in choking, if such complication arises then try at the temperature of 5˚C above the specified temperature. Another issue can be nozzle height, which needs to be properly maintained in the Z direction. In addition, the poor quality of filament can result in the choking of the nozzle head. 

then there are chances of solidification of material, which can cause choking in the nozzle [225]. Nozzle temperature also influences the flexural strength of the printed sample. High nozzle temperature results in good flexural and tensile strength. Low nozzle temperature results in low mechanical properties and is one major cause of nozzle choking [226]. The optimum nozzle temperature settings at which best results can be achieved are different for all materials, which depends on the glass transition temperature and melting temperature of a material. For PLA material, the optimum nozzle temperature is around 200˚C [227]. 

### **8.5 Nozzle materials** 

Nowadays there are nozzles available of different materials like brass, stainless steel, hardened steel, ruby tipped. However, FFF printers generally come with a brass nozzle. When using some special material, a brass nozzle cannot be used every time. Some materials can harm the brass nozzle. Therefore, we need to check and select the nozzle material accordingly. Nozzle made up of brass material is suitable only for printing of nonabrasive materials like PLA, ABS, PETG etc. These are also the most commonly used polymers in FFF [228] which is why most printers have a brass nozzle. To overcome the issue of damaging nozzle hardened steel nozzles can be used as these are more resistant to wear, but as it contains lead, so cannot be used for food materials. For printing related to food materials and print related to direct contact with skin, stainless steel nozzles can be used. For achieving unparalleled precision ruby tipped nozzles can be used. 

### **8.6 Misalignment of the nozzle** 

Misalignment of the nozzle can lead to imperfections and defects in the printed specimen. Misalignment of the nozzle can happen due to improper surface, loose nut and improper timing of belt and servo motor [229]. It can also happen due to very low layer height and can damage the nozzle or result in misalignment of the nozzle, adjustments in the z-axis are done to prevent this [230]. Also, very fast printing speed can lead to misalignment of the nozzle. 

## **9 Process issues** 

### **8.4 Nozzle temperature** 

### **9.1 Printing speed** 

Nozzle temperature is an important factor in FFF. Nozzle temperature has a significant effect on the tensile strength of the printed specimen. Also, nozzle temperature is very important for maintaining the proper flow of extruded material. If there will not be an adequate nozzle temperature 

Printing speed is the amount of material deposited in some given period [231]. Printing speed is an important factor in the 3D printing of any structure. As variation in print speed, directly influence the infill [156]. So, it directly affects the 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2881 

microstructure, strength, dimensional accuracy and cavity present in the structure, printed using FDM printers [18]. Therefore, it becomes an important task to find an optimum value of printing speed, the optimum value of printing speed can be different for different materials used in printing. However, generally for achieving good printing results, the printing speed needs to be in the lower range varying from 40 m/s to 90 m/s [210]. In this optimum range, the printed structure will have high strength, better adhesion and greater dimensional accuracy with fewer cavities. 

affects the tensile compressive and bending properties of the printed structure. Layer Thickness also has a significant contribution in increasing the printer’s speed and resolution. Generally, most FFF printers have the least layer thickness of 0.1 mm. As we increase the layer height, the printer’s speed increases. However, this increase in layer thickness affects the resolution of the printed structure. For achieving fast printing speed and good resolution, we need to optimize layer thickness for every individual FFF printer [21]. Table 4 shows the issue related to printing parameters. 

### **9.2 Travel speed** 

Travel speed represents the speed of head movement of the print head of a printer when it is not extruding any material [232]. By increasing the travel speed of the printer, printing time can be reduced significantly [233]. As we increase, the travel speed to too much extent then it may result in many issues like ringing artefacts and misaligned layers. 

To overcome these issues an optimized travel speed is required. One can start with a travel speed of 100 mm/s and continue with an increment of 5 mm/s until a fine surface is not achieved. If printing quality is compromised then travel speed needs to be decreased. 

### **9.3 Fill pattern and density** 

Infill pattern represents the structure printed inside a model, with the help of slicing software, the infill pattern and infill density for a model can be defined [234]. In FFF by default, the grid pattern is used, but some other printing infill patterns like lines, triangles, and honeycomb, tetrahedral, square and zig-zag patterns can be used [235]. Various infill pattern has their characteristics and contributes to enhancing different properties like strength and surface finish of printing structure. In addition, these patterns are used according to the shape of the structure. For achieving greater strength line, shaped infill pattern is preferred and for high speed, printing honeycomb pattern is preferred. For printing few intrinsic and complex geometry, only selected infill patterns can be used and some compromises are needed to be done i.e., both high speed and strength cannot be achieved simultaneity [236]. In addition, the density of the infill pattern has a significant role in strength and printing time. Greater infill density results in higher strength but will have a large printing time. Low infill density results in less strength and requires less time for printing [237]. 

### **9.4 Layer thickness** 

Layer thickness or layer height is the height of each layer of material extruded by the FFF printer. Layer thickness 

## **10 Development of products for industrial application: Aerospace, Biomedical, automobile, and marine** 

Industrial grade machines, particularly those based on powder bed fusion, are quite expensive to buy and run, but they have excellent print quality and parameters, making them dependable. They can offer a decent return on investment, but this depends greatly on the advantages that 3D printing can bring to each individual situation [247]. The potential of the manufacturing technology should be utilised in every part created for 3D printing. It has been demonstrated, for instance, that in terms of mechanical qualities, WAAM parts can perform better than ones that are conventionally made [248]. This feature, along with the unique geometry optimization capabilities of AM, can significantly reduce weight and waste material while retaining component strength [249]. Carpentry, metallurgy, the machinery and electromechanical industries, industrial automation, heating, ventilation, and air conditioning (HVAC), energy recovery systems, exhaust after treatment systems, corrosion protection systems, fire protection systems, and petrochemicals are just a few of the many industries that benefit greatly from the marine industry [250–257]. 

## **11 Conclusion** 

Following are conclusions of the present study: 

- It has been reported by previous studies that part shrinkage, part shrinkage, high surface roughness, warping from the edges, misaligned part geometry, lack and loss of the adhesion, part distortion, voids and porosity etc., are the major issues in the FFF process. 

- The in case of open source FFF, internal and external factors such as; the variable room temperatures, room humidity, wind speed, heterogeneity in feedstock materials, torsion in feedstock filaments, vibration due to any source, nozzle clogging, nozzle choking, high/low 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2882 

|**Table 4**Issues related to printing<br>parameters|Sr.<br>No.|Material|Infill Parameters<br>Effect Studied|Optimum settings observed / Observations|Ref.|
|---|---|---|---|---|---|
||1|ABS|Nozzle and bed<br>temperatures|It was observed that with an increase in nozzle and<br>bed temperature, the critical crack growth load, actual<br>fracture surface area and the fracture resistance all<br>increased|[238]|
||2|ABS|Layer thickness,<br>raster angle and<br>infill density|Results depicted that optimum results can be achieved<br>at 80% infill % and 0.5 mm layer thickness and 65˚<br>raster angle. Printing with low layer thickness give<br>accurate print results even in intricate designs.<br>f|[203]|
||3|PLA|Raster width,<br>raster angle and<br>layer thickness|The effect of all three parameters used was analysed<br>to check the tensile strength. The highest value is<br>obtained at a 0° raster angle. Due to the higher bond-<br>ing area between the layers having low layer thickness,<br>higher tensile strength was observed. At high values<br>of raster width, tensile strength increased up to some<br>extent after which the presence of void resulted in a<br>decrease in tensile strength.|<br>[239]|
||4|PLA|Infill pattern and<br>infill density|The effect of rectangular, concentric, Hilbert and hon-<br>eycomb patterns at infill densities of 20, 50 and 100%<br>were investigated. The maximum values of tensile<br>strength were achieved using a concentric pattern and<br>the Hilbert pattern displayed the least values.|[240]|
||5|PEEK|Heating tem-<br>perature, printing<br>speed, layer<br>thickness<br>l|<br>It was observed that heating temperature and printing<br>speed have some significant effects on crystallinity.<br>High heating temperature (440 °C), slow printing<br>speed (20 mm/s) and low layer thickness (0.1 mm)<br>are recommended for better surface finish and fewer<br>internal defects.<br>l i|[241]|
||6|PLA|Inflow speed of<br>filament material<br>and layer height|It was observed that at the high speed of inflow fila-<br>ment material, thin layer width will be formed, which<br>will result in less strength. The equal value of layer<br>height and line width results in high strength.<br>f|[242]|
||7|HTPLA|Nozzle<br>temperature|The effect of nozzle temperature on tensile strength<br>was investigated and it was observed that at high<br>nozzle temperature maximum value of tensile strength<br>was achieved. At low nozzle temperature, low bonding<br>was observed.|<br>[243]|
||8|PLA|Nozzle diameter<br>and layer height|The optimum print results for surface roughness were<br>achieved at 0.1 mm layer height and 0.3 mm nozzle<br>diameter. Further decrease in nozzle diameter increase<br>printing time and material consumption.|[244]|
||9|ABS|Build orienta-<br>tion, air gap,<br>raster angle layer<br>width|<br>Air gap shows a significant effect on the storage modu-<br>lus and loss modulus. An increase in storage modulus<br>has been reported with the decrease in the air gap.<br>However, a decrease in raster angle, build orientation,<br>and layer width improves the storage modulus and loss<br>modulus.|<br>[245]|
||10|PLA|Nozzle<br>temperature|It was observed that nozzle temperature must be set<br>to200°C for increasingthermal stability|[246]|



nozzle and bed temperature are conducive for the mentioned issues. 

- The above defects can be minimized or eliminated by chemical, laser, heat or ultrasound treatments. 

- In the case of 3D printing, more specifically in the filaments, the concentration of excessive humidity can cause a long list of problems, all with the same end, a 3D printing failed. The effects of attracting water can lead to the following problems: increased fragility, increased diameter (possible problems with printers with Bowden 

type extrusion system), filament degradation, breaking filament, etc. Preheating of the feedstock filaments before 3D printing at 50–70 ̊C. 

- Generally, most of the plastics and metals shrink after melting and depositing, so every time some allowance is taken for safety especially in the case of metals. In FFF 3D printing some materials shrink more and some materials don’t shrink. The main reason for the shrinkage of plastic is when the temperature is high. 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2883 

- The most popular post-processing technique to improve the mechanical performance of FDM prints is heat treatment, often known as annealing. The layer-to-layer gaps are filled when heat is applied to the component, resulting in a smoother surface. The substance flows on the surface as a result of the molecular surface tension being reduced as a result of the viscosity reduction at the glass transition temperature. A finer surface finish and greater mechanical qualities are produced by the material’s reflow, which fills up porous spaces, gaps, and staircase effects within layers. 

- Misalignment of print bed leads to deformation in the printed product. The misalignment in print bed leads to issues like the improper first layer, leaning prints, weak and deformed infill, layer separation and surface quality. As a result, the desired product will lack in strength, dimensional, accuracy and will be full of many defects. Hence it becomes very necessary to eliminate the misalignment of print beds to achieve good print quality. 

**Funding** The author(s) of this article has not received funding in any form from any financial body/Institution. 

### **Declarations** 

**Declaration of conflicting interests** There are no potential conflicts of interest among all authors. 

**Ethical concerns** Not required. 

## **References** 

1. Singh, R., et al.: Effect of single particle size, double particle size and triple particle size Al2O3 in Nylon-6 matrix on mechanical properties of feed stock filament for FDM. Compos. Part B: Eng. **106** , 20–27 (2016) 

2. Moumen, E., Ahmed, M., Tarfaoui, Lafdi, K.: “Additive manufacturing of polymer composites: Processing and modeling approaches.“. Compos. Part B: Eng. **171** , 166–182 (2019) 

3. Moury, B., Cécile, D.: “Host range evolution of potyviruses: A global phylogenetic analysis.“ Viruses 12, no. 1 : p. 111. (2020) 

4. Bansal, G., et al.: “Microstructural characterization, applications and process study of various additive manufacturing process: a review.“ Materials Today: Proceedings (2020) 

5. Haleem, A., Javaid, M.: 3D printed medical parts with different materials using additive manufacturing. Clin. Epidemiol. Global Health. **8** (1), 215–223 (2020) 

6. Sivarupan, T., et al.: “Reduced consumption of materials and hazardous chemicals for energy efficient production of metal parts through 3D printing of sand molds.“Journal of cleaner production224: pp. 411–420. (2019) 

7. Szymczyk, P., et al.: “A review of fabrication polymer scaffolds for biomedical applications using additive manufacturing techniques.“Biocybernetics and Biomedical Engineering(2020) 

8. Fasel, U., et al.: “Composite additive manufacturing of morphing aerospace structures.“. Manuf. Lett. **23** , 85–88 (2020) 

9. Wang, D., et al.: Research on design optimization and manufacturing of coating pipes for automobile seal based on selective laser melting. J. Mater. Process. Technol. **273** , 116227 (2019) 

10. Virgin, L.N.: “Enhancing the teaching of elastic buckling using additive manufacturing. " Eng. Struct. **174** , 338–345 (2018) 

11. Liu, B., et al.: Creating metal parts by fused deposition modeling and sintering. Mater. Lett. **263** , 127252 (2020) 

12. Juskova, P., et al.: “Resolution improvement of 3D stereolithography through the direct laser trajectory programming: Application to microfluidic deterministic lateral displacement device.“Analytica chimica acta1000: pp. 239–247. (2018) 

13. Elsayed, H., et al.: “Novel bioceramics from digital light processing of calcite/acrylate blends and low temperature pyrolysis.“Ceramics International(2020) 

14. Liu, K., et al.: Effects of raw material ratio and post-treatment on properties of soda lime glass-ceramics fabricated by selective laser sintering. Ceram. Int. **46** , 13 (2020) 

15. Zhao, R., et al.: “Selective laser melting of elemental powder blends for fabrication of homogeneous bulk material of neareutectic Ni–Sn composition.“Additive Manufacturing: p.101261. (2020) 

16. Shu, X., Wang, R.: Thermal residual solutions of beams, plates and shells due to laminated object manufacturing with gradient cooling. Compos. Struct. **174** , 366–374 (2017) 

17. Wong, H., et al.: Material characterisation using electronic imaging for Electron Beam Melting process monitoring. Manuf. Lett. **23** , 44–48 (2020) 

18. Heidari-Rarani, Mohammad, M., Rafiee-Afarani, Zahedi, A.M.: Mechanical characterization of FDM 3D printing of continuous carbon fiber reinforced PLA composites. Compos. Part B: Eng. **175** , 107147 (2019) 

19. Jakus, A.E.: “An Introduction to 3D Printing—Past, Present, and Future Promise.“ 3D Printing in Orthopaedic Surgery, pp. 1–15. Elsevier (2019) 

20. Nofar, M.: and Chul B. Park. Polylactide Foams: Fundamentals, Manufacturing, and Applications. William Andrew (2017) 

21. Khabia, S., Kamlesh, K., Jain: “Influence of change in layer thickness on mechanical properties of components 3D printed on Zortrax M 200 FDM printer with Z-ABS filament material & Accucraft i250 + FDM printer with low cost ABS filament material.“ Materials Today: Proceedings (2020) 

22. Sodeifian, G., Ghaseminejad, S.: “Preparation of polypropylene/ short glass fiber composite as Fused Deposition Modeling (FDM) filament. Results in Physics. **12** , 205–222 (2019) 

23. Garzon-Hernandez, S., et al.: Design of FDM 3D printed polymers: An experimental-modelling methodology for the prediction of mechanical properties. Mater. Design. **188** , 108414 (2020) 

24. Rahman, H., et al.: “Investigation on the Scale Factor applicable to ABS based FDM Additive Manufacturing.“ Materials Today: Proceedings 5.1 : pp. 1640–1648. (2018) 

25. Kerekes, T., Webbe, et al.: Characterization of process–deformation/damage property relationship of fused deposition modeling (FDM) 3D-printed specimens. Additive Manuf. **25** , 532–544 (2019) 

26. Araya-Calvo, M., et al.: Evaluation of compressive and flexural properties of continuous fiber fabrication additive manufacturing technology. Additive Manuf. **22** , 157–164 (2018) 

27. Riddick, J.C., et al.: Fractographic analysis of tensile failure of acrylonitrile-butadiene-styrene fabricated by fused deposition modeling. Additive Manuf. **11** , 49–59 (2016) 

28. McLouth, T.D., et al.: The impact of print orientation and raster pattern on fracture toughness in additively manufactured ABS. Additive Manuf. **18** , 103–109 (2017) 

29. Liu, Z., Xing, S.: Mechanical characteristics of wood, ceramic, metal and carbon fiber-based PLA composites fabricated by FDM. J. Mater. Res. Technol. **8** (5), 3741–3751 (2019) 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2884 

30. Abdullah, A., Manaf, et al.: “Mechanical and physical properties of highly ZrO2/β-TCP filled polyamide 12 prepared via fused deposition modelling (FDM) 3D printer for potential craniofacial reconstruction application.“. Mater. Lett. **189** , 307–309 (2017) 

31. Lay, M., et al.: Comparison of physical and mechanical properties of PLA, ABS and nylon 6 fabricated using fused deposition modeling and injection molding. Compos. Part B: Eng. **176** , 107341 (2019) 

32. Singh, R., et al.: Investigation for surface finish improvement of FDM parts by vapor smoothing process. Compos. Part B: Eng. **111** , 228–234 (2017) 

33. Niknam, H., et al.: “3D Printed Accordion-like Materials: A Design Route to Achieve Ultrastretchability.“Additive Manufacturing: p.101215. (2020) 

34. Guerrero-de-Mier, A., Espinosa, M.M., Domínguez, M.: Bricking: A new slicing method to reduce warping. Procedia Eng. **132** , 126–131 (2015) 

35. Minetola, P., Galati, M.: A challenge for enhancing the dimensional accuracy of a low-cost 3D printer by means of self-replicated parts. Additive Manuf. **22** , 256–264 (2018) 

36. Elsholtz, C., Harper, A.: Additive decompositions of sets with restricted prime factors. Trans. Am. Math. Soc. **367** (10), 7403– 7427 (2015) 

37. Allen, R.J.A.: Trask. “An experimental demonstration of effective Curved Layer Fused Filament Fabrication utilising a parallel deposition robot. Additive Manuf. **8** , 78–87 (2015) 

38. Coasey, K., et al.:“Nonisothermal Welding in Fused Filament Fabrication.“ Additive Manufacturing: p.101140. (2020) 

39. Lee, C.-Y., Chung-Yin, L.: The influence of forced-air cooling on a 3D printed PLA part manufactured by fused filament fabrication. Additive Manuf. **25** , 196–203 (2019) 

40. Shariatnia, S., et al.: Atomization of cellulose nanocrystals aqueous suspensions in fused deposition modeling: A scalable technique to improve the strength of 3D printed polymers. Compos. Part B: Eng. **177** , 107291 (2019) 

41. Hussey, B., et al.: Light-weight/defect-tolerant topologically selfinterlocking polymeric structure by fused deposition modeling. Compos. Part B: Eng. **183** , 107700 (2020) 

42. Chohan, J., Singh, et al.: Dimensional accuracy analysis of coupled fused deposition modeling and vapour smoothing operations for biomedical applications. Compos. Part B: Eng. **117** , 138–149 (2017) 

43. Nober, C., et al.: Feasibility study into the potential use of fuseddeposition modeling to manufacture 3D-printed enteric capsules in compounding pharmacies. Int. J. Pharm. **569** , 118581 (2019) 

44. Ilyés, K., et al.: “The applicability of pharmaceutical polymeric blends for the fused deposition modelling (FDM) 3D technique: Material considerations–printability–process modulation, with consecutive effects on in vitro release, stability and degradation.“. Eur. J. Pharm. Sci. **129** , 110–123 (2019) 

45. Gebreyes, W.A., et al.: An integrated fluidic electrochemical sensor manufactured using fused filament fabrication and supersonic cluster beam deposition. Sens. Actuators A: Phys. **301** , 111706 (2020) 

46. Chohan, J., Singh, R., Singh, Kamaljit Singh, B.: Mathematical modelling of surface roughness for vapour processing of ABS parts fabricated with fused deposition modelling. J. Manuf. Process. **24** , 161–169 (2016) 

47. Palmero, E.M., et al.: “Composites based on metallic particles and tuned filling factor for 3D-printing by Fused Deposition Modeling.“ Composites Part. Appl. Sci. Manuf. **124** , 105497 (2019) 

48. Puigoriol-Forcada, J.M., et al.: Flexural fatigue properties of polycarbonate fused-deposition modelling specimens. Mater. Design. **155** , 414–421 (2018) 

49. de Toro, E., Verdejo, et al.: “Analysis of the influence of the variables of the Fused Deposition Modeling (FDM) process on the 

mechanical properties of a carbon fiber-reinforced polyamide. " Procedia Manufacturing. **41** , 731–738 (2019) 

50. Ranjan, N., Singh, R., Inderpreet, S., Ahuja: “Preparation of partial denture with nano HAp-PLA composite under cryogenic grinding environment using 3D printing.“ :517–522. (2020) 

51. Kuki, Ã., et al.: Fast identification of phthalic acid esters in poly (vinyl chloride) samples by direct analysis in real time (DART) tandem mass spectrometry. Int. J. Mass Spectrom. **303** , 2–3 (2011) 

52. Kousiatza, C., Karalekas, D.: In-situ monitoring of strain and temperature distributions during fused deposition modeling process. Mater. Design. **97** , 400–406 (2016) 

53. Guo, R., et al.: “Effect of toughening agents on the properties of poplar wood flour/poly (lactic acid) composites fabricated with fused deposition modeling.“. Eur. Polymer J. **107** , 34–45 (2018) 

54. Waran, V., et al.: Utility of multimaterial 3D printers in creating models with pathological entities to enhance the training experience of neurosurgeons. J. Neurosurg. **120** (2), 489–492 (2014) 

55. Ranjan, N., Singh, R.: and I. P. S. Ahuja. “Investigations on joining of orthopaedic scaffold with rapid tooling.“ Proceedings of the Institution of Mechanical Engineers, Part H: Journal of Engineering in Medicine 233, no. 7 : 754–760. (2019) 

56. Madamesila, J., et al.: Characterizing 3D printing in the fabrication of variable density phantoms for quality assurance of radiotherapy. Physica Med. **32** (1), 242–247 (2016) 

57. Pringle, A.M., Rudnicki, M., Joshua, M.: Pearce. “Wood Furniture Waste–Based Recycled 3-D Printing Filament.“. For. Prod. J. **68** (1), 86–95 (2018) 

58. Mueller, S., et al.: “WirePrint: 3D printed previews for fast prototyping.“ Proceedings of the 27th annual ACM symposium on User interface software and technology. (2014) 

59. Singh, R., Kumar, R., Ranjan, N.: Sustainability of recycled ABS and PA6 by banana fiber reinforcement: thermal, mechanical and morphological properties. J. Institution Eng. (India): Ser. C. **100** (2), 351–360 (2019) 

60. Deshpande, S., Prashant, et al.: “DEVELOPING AN OPEN SOURCE, INEXPENSIVE, LARGE-SCALE POLAR CONFIGURATION 3D PRINTER.“International Journal of Engineering Research & Innovation: p.13. (2019) 

61. Straub, J.: “Initial work on the characterization of additive manufacturing (3D printing) using software image analysis.“ Machines 3.2 : pp. 55–71. (2015) 

62. Schmitt, B., Madeira, et al.: “A comparative study of cartesian and delta 3D printers on producing PLA parts.“. Mater. Res. **20** , 883–886 (2017) 

63. Salentijn, G.I.J., et al.: Fused deposition modeling 3D printing for (bio) analytical device fabrication: procedures, materials, and applications. Anal. Chem. **89** , 13 (2017) 

64. Fafenrot, S., et al.: Three-dimensional (3D) printing of polymermetal hybrid materials by fused deposition modeling. Materials. **10** (10), 1199 (2017) 

65. Motyl, B., et al.: “How will change the future engineers’ skills in the Industry 4.0 framework? A questionnaire survey.“. Procedia Manuf. **11** , 1501–1509 (2017) 

66. Vélez, M., Toala, E., Juan Cristóbal, Z.: Koala 3D: A continuous climbing 3D printer. Robot. Comput. Integr. Manuf. **64** , 101950 (2020) 

67. Asif, M., et al.: “A new photopolymer extrusion 5-axis 3D printer.“. Additive Manuf. **23** , 355–361 (2018) 

68. Zi, B., et al.: Design, stiffness analysis and experimental study of a cable-driven parallel 3D printer. Mech. Mach. Theory. **132** , 207–222 (2019) 

69. Zhang, Z., Shao, Z., Wang, L.: Optimization and implementation of a high-speed 3-DOFs translational cable-driven parallel robot. Mech. Mach. Theory. **145** , 103693 (2020) 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2885 

70. Yuan, H., Deblaise, D.: Static and dynamic stiffness analyses of cable-driven parallel robots with non-negligible cable mass and elasticity. Mech. Mach. Theory. **85** , 64–81 (2015) 

71. Alikhani, A., et al.: “Workspace analysis of a three DOF cabledriven mechanism.“Journal of Mechanisms and Robotics1.4 (2009) 

72. Sun, J., et al.: Extrusion-based food printing for digitalized food design and nutrition control. J. Food Eng. **220** , 1–11 (2018) 

73. Sun, J., et al.: “3D Food Printing: Perspectives.“ Polymers for Food Applications, pp. 725–755. Springer, Cham (2018) 

74. Hager, I., Golonka, A., Putanowicz, R.: “3D printing of buildings and building components as the future of sustainable construction? " Procedia Engineering. **151** , 292–299 (2016) 

75. McClinton, E., Wylie, B., Carl, A., Moore Jr.: “Creating a High and Homogenous Resolution Workspace for SCARA Based 3D Printers.“ IOP Conference Series: Materials Science and Engineering. Vol. 689. No. 1. IOP Publishing, (2019) 

76. Ogulmuş, A., Saygın, A., Çakan: “Modeling And Position Control Of Scara Type 3D Printer.“. Int. J. Sci. Technol. Res. **5** , 140– 143 (2016) 

77. Wang, L., Jing, Liu: Liquid phase 3D printing for quickly manufacturing conductive metal objects with low melting point alloy ink. Sci. China Technological Sci. **57** (9), 1721–1728 (2014) 

78. Pietrzak, K., Isreb, A., Mohamed, A.: Alhnan. “A flexible-dose dispenser for immediate and extended-release 3D printed tablets. Eur. J. Pharm. Biopharm. **96** , 380–387 (2015) 

79. Gu, J., et al.: Characterization of particulate and gaseous pollutants emitted during operation of a desktop 3D printer. Environ. Int. **123** , 476–485 (2019) 

80. Xia, M., Nematollahi, B., Sanjayan, J.: Printability, accuracy and strength of geopolymer made using powder-based 3D printing for construction applications. Autom. Constr. **101** , 179–189 (2019) 

81. Kreiger, M., Joshua, M., Pearce: ACS Sustain. Chem. Eng. **1** (12), 1511–1519 (2013). “Environmental life cycle analysis of distributed three-dimensional printing and conventional manufacturing of polymer products.“ 

82. Le Duigou, A., et al.: 3D printing of wood fibre biocomposites: From mechanical to actuation functionality. Mater. Design. **96** , 106–114 (2016) 

83. Kariz, M., Sernek, M., Manja Kitek Kuzman: Effect of humidity on 3D-printed specimens from wood-PLA filaments. Wood Res. **63** , 917–922 (2018) 

84. Tan, J.C., Low, H.Y.: Embedded electrical tracks in 3D printed objects by fused filament fabrication of highly conductive composites. Additive Manuf. **23** , 294–302 (2018) 

85. Ivey, M., et al.: Characterizing short-fiber-reinforced composites produced using additive manufacturing. Adv. Manufacturing: Polym. Compos. Sci. **3** (3), 81–91 (2017) 

86. Mbow, M., Mansour, P.R., Marin, Franck Pourroy: and. “Extruded diameter dependence on temperature and velocity in the fused deposition modeling process.“Progress in Additive Manufacturing: pp.1–14. (2020) 

87. Squires, A.D., Lewis, R.A.: Feasibility and characterization of common and exotic filaments for use in 3D printed terahertz devices. J. Infrared Millim. Terahertz Waves. **39** , 7 (2018) 

88. Halidi, M.: Effects Of Moisture On Acrylonitrile Butadiene Styrene (Abs) Filament Material. In: Fused Deposition Modeling (Fdm) Rapid Prototyping Machine. Diss. Universiti Sains Malaysia (2013) 

89. Carneiro, O.S., Silva, A.F.: and Rui Gomes. “Fused deposition modeling with polypropylene.“ Materials & Design. **83** , 768–776 (2015) 

90. Zhou, Y., et al.: From 3D to 4D printing: approaches and typical applications. J. Mech. Sci. Technol. **29** (10), 4281–4288 (2015) 

91. Ionita, C.N., et al.: “Challenges and limitations of patient-specific vascular phantom fabrication using 3D Polyjet printing.“ Medical 

Imaging 2014: Biomedical Applications in Molecular, Structural, and Functional Imaging, vol. 9038. International Society for Optics and Photonics (2014) 

92. Kroll, E., Artzi, D.: “Enhancing aerospace engineering students’ learning with 3D printing wind-tunnel models.“Rapid Prototyping Journal(2011) 

93. Yuan, P.F., et al.: “Robotic multi-dimensional printing based on structural performance.“ Robotic Fabrication in Architecture, Art and Design 2016, pp. 92–105. Springer, Cham (2016) 

94. Sanjayan, J.G., et al.: Effect of surface moisture on inter-layer strength of 3D printed concrete. Constr. Build. Mater. **172** , 468– 475 (2018) 

95. Klodowski, A., Eskelinen, H., Scott Semken: and. “Leakageproof nozzle design for RepRap community 3D printer.“ Robotica 33.4 : p.721. (2015) 

96. Ramani, K., Borgaonkar, H., Hoyle, C.: Experiments on compression moulding and pultrusion of thermoplastic powder impregnated towpregs. Compos. Manuf. **6** (1), 35–43 (1995) 

97. Heckele, M., Schomburg, W.K.: Review on micro molding of thermoplastic polymers. J. Micromech. Microeng. **14** (3), R1 (2003) 

98. Wang, D., Bor-Sen Chiou: A high‐throughput, controllable, and environmentally benign fabrication process of thermoplastic nanofibers. Macromol. Mater. Eng. **292** (4), 407–414 (2007) 

99. Thunwall, M., Boldizar, A., Mikael Rigdahl: “Compression molding and tensile properties of thermoplastic potato starch materials.“ Biomacromolecules. **7** (3), 981–986 (2006) 

100. Kishi, H., et al.: Damping properties of thermoplastic-elastomer interleaved carbon fiber-reinforced epoxy composites. Compos. Sci. Technol. **64** , 2517–2523 (2004) 

101. Bader, M.G., Bowyer, W.H.: The mechanical properties of thermoplastics strengthened by short discontinuous fibres. J. Phys. D. **5** (12), 2215 (1972) 

102. Starosolski, Z.A., et al.: Application of 3-D printing (rapid prototyping) for creating physical models of pediatric orthopedic disorders. Pediatr. Radiol. **44** (2), 216–221 (2014) 

103. Dry, C.: Procedures developed for self-repair of polymer matrix composite materials. Compos. Struct. **35** (3), 263–269 (1996) 

104. Tham, L.M., Gupta, M., Cheng, L.: Effect of limited matrix–reinforcement interfacial reaction on enhancing the mechanical properties of aluminium–silicon carbide composites. Acta Mater. **49** , 16 (2001) 

105. WU, Xing-chao, and, He-guo, Z.H.U.: “Progress of Preparation Technology of Silicon Carbide Particle Reinforced Aluminum Matrix Composites [J].“Shanghai Nonferrous Metals3 (2012) 

106. Murphy, C.A., Maurice, N.: Collins. “Microcrystalline cellulose reinforced polylactic acid biocomposite filaments for 3D printing.“. Polym. Compos. **39** (4), 1311–1320 (2018) 

107. Zhang, D., et al.: “Fabrication of highly conductive graphene flexible circuits by 3D printing.“. Synth. Met. **217** , 79–86 (2016) 

108. Zhang, Q., Gao, Y., Jing, Liu: Atomized spraying of liquid metal droplets on desired substrate surfaces as a generalized way for ubiquitous printed electronics. Appl. Phys. A. **116** (3), 1091–1097 (2014) 

109. Woirgard, J., et al.: Study of the mechanical properties of ceramic materials by the nanoindentation technique. J. Eur. Ceram. Soc. **18** , 15 (1998) 

110. Abdrakhimov, V.Z., Abdrakhimova, E.S.: Study of phase composition of ceramic materials based on nonferrous metallurgy, chemical, and petrochemical industry aluminum-containing waste. Refract. Ind. Ceram. **56** (1), 5–10 (2015) 

111. Kalita, S.J., Bhardwaj, A., Himesh, A., Bhatt: “Nanocrystalline calcium phosphate ceramics in biomedical engineering.“ Materials Science and Engineering: C. **27** (3), 441–449 (2007) 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2886 

112. Leigh, S.J., et al.: “A simple, low-cost conductive composite material for 3D printing of electronic sensors.“. PloS one. **7** (11), e49365 (2012) 

113. Froes, F., Boyer, R., Dutta, B.: “Introduction to aerospace materials requirements and the role of additive manufacturing.“ Additive manufacturing for the aerospace industry, pp. 1–6. Elsevier (2019) 

114. Lombardi, J.L., et al.: “Issues associated with EFF & FDM ceramic filled feedstock formulation.“ 1997 International Solid Freeform Fabrication Symposium. (1997) 

115. Eckel, Z.C., et al.: “Additive manufacturing of polymer-derived ceramics. " Sci. **351** , 6268 (2016) 

116. Hwang, S., et al.: Thermo-mechanical characterization of metal/ polymer composite filaments and printing parameter study for fused deposition modeling in the 3D printing process. J. Electron. Mater. **44** (3), 771–777 (2015) 

117. Mellin, P., et al.: Nano-sized by-products from metal 3D printing, composite manufacturing and fabric production. J. Clean. Prod. **139** , 1224–1233 (2016) 

118. Vanderploeg, A., Lee, S.-E., Mamp, M.: The application of 3D printing technology in the fashion industry. Int. J. Fashion Des. Technol. Educ. **10** (2), 170–179 (2017) 

119. Debroy, T., et al.: “Scientific, technological and economic issues in metal printing and their solutions.“Nature materials: p.1. (2019) 

120. Sames, W.J., et al.: The metallurgy and processing science of metal additive manufacturing. Int. Mater. Rev. **61** (5), 315–360 (2016) 

121. Panicker, C.T., Justus, C., Boopathi, Vivekanandan, R.: “Comparing the Geometrical Accuracy of a 3D Printed Pattern to a Metal Pattern.“ IOP Conference Series: Materials Science and Engineering. Vol. 561. No. 1. IOP Publishing, (2019) 

122. Godoi, F.C., Prakash, S., Bhesh, R., Bhandari: 3d printing technologies applied for food design: Status and prospects. J. Food Eng. **179** , 44–54 (2016) 

123. Sun, J., et al.: A review on 3D printing for customized food fabrication. Procedia Manuf. **1** , 308–319 (2015) 

124. Lanaro, M., et al.: 3D printing complex chocolate objects: Platform design, optimization and evaluation. J. Food Eng. **215** , 13–22 (2017) 

125. Liu, Z., et al.: Impact of rheological properties of mashed potatoes on 3D printing. J. Food Eng. **220** , 76–82 (2018) 

126. Sun, J., et al.: “An overview of 3D printing technologies for food fabrication.“ Food and bioprocess technology 8.8 : pp. 1605– 1615. (2015) 

127. Kumar, S., et al.: Investigations for mechanical, thermal and magnetic properties of polymeric composite matrix for four-dimensional printing applications. J. Brazilian Soc. Mech. Sci. Eng. **42** (4), 1–15 (2020) 

128. Kang, H.-W., et al.: A 3D bioprinting system to produce humanscale tissue constructs with structural integrity. Nat. Biotechnol. **34** (3), 312–319 (2016) 

129. Cui, H., et al.: 3D bioprinting for organ regeneration. Adv. Healthc. Mater. **6** (1), 1601118 (2017) 

130. Lee, J., Min: and Wai Yee Yeong. “Design and printing strategies in 3D bioprinting of cell-hydrogels: A review.“ Advanced healthcare materials 5.22 : pp. 2856–2865. (2016) 

131. Ning, L., Chen, X.: “A brief review of extrusion-based tissue scaffold bio‐printing. " Biotechnol. J. **12** , 1600671 (2017) 

132. Li, J., et al.: Recent advances in bioprinting techniques: approaches, applications and future prospects. J. translational Med. **14** (1), 271 (2016) 

133. Pourchet, L.J., et al.: Human skin 3D bioprinting using scaffoldfree approach. Adv. Healthc. Mater. **6** (4), 1601101 (2017) 

134. Yang, D., et al.: “Fibre flow and void formation in 3D printing of short-fibre reinforced thermoplastic composites: An experimental benchmark exercise.“Additive Manufacturing: p.101686. (2020) 

135. Gavali, V.C., Pravin, R., Kubade, Hrushikesh, B.: Kulkarni. “Mechanical and Thermo-mechanical Properties of Carbon fiber Reinforced Thermoplastic Composite Fabricated Using Fused Deposition Modeling Method.“ Materials Today: Proceedings 22 : pp. 1786–1795. (2020) 

136. Cowley, A., et al.: Effects of variable gravity conditions on additive manufacture by fused filament fabrication using polylactic acid thermoplastic filament. Additive Manuf. **28** , 814–820 (2019) 

137. Lee, J., et al.: “Fabrication of poly (lactic acid)/Ti composite scaffolds with enhanced mechanical properties and biocompatibility via fused filament fabrication (FFF)–based 3D printing.“. Additive Manuf. **30** , 100883 (2019) 

138. Goulas, A., et al.: “Fused filament fabrication of functionally graded polymer composites with variable relative permittivity for microwave devices.“Materials & Design: p.108871. (2020) 

139. Chueh, Y.-H., et al.: Integrated laser-based powder bed fusion and fused filament fabrication for three-dimensional printing of hybrid metal/polymer objects. Additive Manuf. **31** , 100928 (2020) 

140. Lee, G., et al.: Fabrication of ceramic bone scaffolds by solvent jetting 3D printing and sintering: towards load-bearing applications. Additive Manuf. **33** , 101107 (2020) 

141. Sudan, K., et al.: “Processing of hydroxyapatite and its composites using ceramic fused filament fabrication (CF3).“ Ceramics International 46.15 : pp.23922–23931. (2020) 

142. De León, A.S., Domínguez-Calvo, A., Molina, S.I.: Materials with enhanced adhesive properties based on acrylonitrile-butadiene-styrene (ABS)/thermoplastic polyurethane (TPU) blends for fused filament fabrication (FFF). Mater. Design. **182** , 108044 (2019) 

143. Gibson, M.A., et al.: 3D printing metals like thermoplastics: Fused filament fabrication of metallic glasses. Mater. Today. **21** , 697–702 (2018) 

144. Singh, G., et al.: “Copper extrusion 3D printing using metal injection moulding feedstock: analysis of process parameters for green density and surface roughness optimization.“Additive Manufacturing: p.101778. (2020) 

145. Lille, M., et al.: “Structural and textural characteristics of 3D-printed protein-and dietary fibre-rich snacks made of milk powder and wholegrain rye flour.“ Foods 9.11 : p. 1527. (2020) 

146. Derossi, A., et al.: Analyzing the effects of 3D printing process per se on the microstructure and mechanical properties of cereal food products. Innovative Food Science & Emerging Technologies. **66** , 102531 (2020) 

147. Maniglia, B.C., et al.: “Dry heating treatment: A potential tool to improve the wheat starch properties for 3D food printing application.“. Food Res. Int. **137** , 109731 (2020) 

148. Yang, J., et al.: “Cellulose, hemicellulose, lignin, and their derivatives as multi-components of bio-based feedstocks for 3D printing.“Carbohydrate Polymers: p.116881. (2020) 

149. Singh, P., et al.: “Printability studies of Ti-6Al-4 V by metal fused filament fabrication (MF3).“International Journal of Refractory Metals and Hard Materials: p.105249. (2020) 

150. Alberts, E., et al.: “Impact of metal additives on particle emission profiles from a fused filament fabrication 3D printer.“. Atmos. Environ. **244** , 117956 (2021) 

151. Gilmer, E.L., et al.: Model analysis of feedstock behavior in fused filament fabrication: Enabling rapid materials screening. Polymer. **152** , 51–61 (2018) 

152. Ganesan, K., et al.: “Structural, Raman and photoluminescence studies on nanocrystalline diamond films: Effects of ammonia in feedstock.“Diamond and Related Materials: p.107872. (2020) 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2887 

153. Díaz-García, Ã., et al.: “Novel procedure for laboratory scale production of composite functional filaments for additive manufacturing.“. Mater. Today Commun. **24** , 101049 (2020) 

154. Angelopoulos, P.M., Samouhos, M., Taxiarchou, M.: “Functional fillers in composite filaments for fused filament fabrication; a review.“ Materials Today: Proceedings (2020) 

155. Sikder, P., et al.: “Bioactive amorphous magnesium phosphatepolyetheretherketone composite filaments for 3D printing.“Dental Materials(2020) 

156. Geng, P., et al.: Effects of extrusion speed and printing speed on the 3D printing stability of extruded PEEK filament. J. Manuf. Process. **37** , 266–273 (2019) 

157. Parsons, P., et al.: “Fabrication of low dielectric constant composite filaments for use in fused filament fabrication 3D printing.“. Additive Manuf. **30** , 100888 (2019) 

158. Singh, R., Singh, S., Mankotia, K.: “Development of ABS based wire as feedstock filament of FDM for industrial applications.“Rapid Prototyping Journal(2016) 

159. Ebel, E.: and Thorsten Sinnemann. “Fabrication of FDM 3D objects with ABS and PLA and determination of their mechanical properties.“ RTejournal 2014.1(2014) 

160. Wu, G., et al.: Solid freeform fabrication of metal components using fused deposition of metals. Mater. Design. **23** (1), 97–105 (2002) 

161. Galantucci, L., Maria, et al.: Analysis of dimensional performance for a 3D open-source printer based on fused deposition modeling technique. Procedia Cirp. **28** , 82–87 (2015) 

162. Stoof, D., Pickering, K.: Sustainable composite fused deposition modelling filament using recycled pre-consumer polypropylene. Compos. Part B: Eng. **135** , 110–118 (2018) 

163. Aho, J., et al.: Roadmap to 3D-printed oral pharmaceutical dosage forms: feedstock filament properties and characterization for fused deposition modeling. J. Pharm. Sci. **108** (1), 26–35 (2019) 

164. Asp, L.E., Coast, G.: Queensland, Australia : pp. 322–331. (1997) 165. Bos, F.P., et al.: “3D printing concrete with reinforcement. In: High Tech Concrete: Where Technology and Engineering Meet, pp. 2484–2493. Springer, Cham (2018) 

166. Dumas, J.E., et al.: Synthesis and characterization of an injectable allograft bone/polymer composite bone void filler with tunable mechanical properties. Tissue Eng. Part A. **16** , 8 (2010) 

167. Masood, S.H., Song, W.Q.: Development of new metal/polymer materials for rapid tooling using fused deposition modelling. Mater. Design. **25** , 7 (2004) 

168. Blok, L.G., et al.: An investigation into 3D printing of fibre reinforced thermoplastic composites. Additive Manuf. **22** , 176–186 (2018) 

169. Yakout, M., et al.: “The selection of process parameters in additive manufacturing for aerospace alloys.“. Int. J. Adv. Manuf. Technol. **92** , 5–8 (2017) 

170. Boparai, K., Singh, R., Singh, Singh, H.: “Experimental investigations for development of Nylon6-Al-Al2O3 alternative FDM filament.“Rapid Prototyping Journal(2016) 

171. Kukla, C., et al.: “Properties for PIM Feedstocks Used in Fused Filament Fabrication.“ World PM2016-AM-Deposition Technologies (2016) 

172. Dave, H.K., et al.: “Open hole tensile testing of 3D printed parts using in-house fabricated PLA filament.“Rapid Prototyping Journal(2020) 

173. Mostafa, N., et al.: A study of melt flow analysis of an ABS-Iron composite in fused deposition modelling process. Tsinghua Sci. Technol. **14** , 29–37 (2009) 

174. Wang, G., et al.: CHI Conference on Human Factors in Computing Systems. 2018. (2018) 

175. Corcione, C., Esposito, et al.: One-step solvent-free process for the fabrication of high loaded PLA/HA composite filament for 3D printing. J. Therm. Anal. Calorim. **134** (1), 575–582 (2018) 

176. Widmer, M.S., et al.: Manufacture of porous biodegradable polymer conduits by an extrusion process for guided tissue regeneration. Biomaterials. **19** , 1945–1955 (1998) 

177. Muller, M., Thomas, et al.: Influence of feeding conditions in twin-screw extrusion of PP/MWCNT composites on electrical and mechanical properties. Compos. Sci. Technol. **71** , 13 (2011) 

178. Benbow, J.J., Oxley, E.W., Bridgwater, J.: The extrusion mechanics of pastes—the influence of paste formulation on extrusion parameters. Chem. Eng. Sci. **42** (9), 2151–2162 (1987) 

179. Turner, B.N., Strong, R., Scott, A.: Gold. “A review of melt extrusion additive manufacturing processes: I. Process design and modeling.“Rapid Prototyping Journal(2014) 

180. Ning, F., et al.: Additive manufacturing of carbon fiber reinforced thermoplastic composites using fused deposition modeling. Compos. Part B: Eng. **80** , 369–378 (2015) 

181. Sa’ude, N., et al.: “Dynamic mechanical properties of copperABS composites for FDM feedstock.“. Int. J. Eng. Res. Appl. **3** (3), 1257–1263 (2013) 

182. Rhodes, C.G., Anthony, W.: Thompson. “The composition dependence of stacking fault energy in austenitic stainless steels. Metall. Trans. A. **8** (12), 1901–1906 (1977) 

183. Gurland, J., Bardzil, P.: “Relation of strength, composition, and grain size of sintered WC-Co alloys.“ Jom 7.2 : pp.311–315. (1955) 

184. Alaimo, G., et al.: Influence of meso-structure and chemical composition on FDM 3D-printed parts. Compos. Part B: Eng. **113** , 371–380 (2017) 

185. Suarez, H., Barlow, J.W., Paul, D.R.: Mechanical properties of ABS/polycarbonate blends. J. Appl. Polym. Sci. **29** (11), 3253– 3259 (1984) 

186. Bhambri, Y., et al.: Effect of composition and cooling rate on the transformation of α to γ phase in TiAl alloys. Mater. Sci. Engineering: A. **424** (1–2), 361–365 (2006) 

187. Kumari, R., et al.: Fundamental studies on wood/cellulose-plastic composites: effects of composition and cellulose dimension on the properties of cellulose/PP composite. J. wood Sci. **53** (6), 470– 480 (2007) 

188. Leu, S.-Y., et al.: Optimized material composition to improve the physical and mechanical properties of extruded wood–plastic composites (WPCs). Constr. Build. Mater. **29** , 120–127 (2012) 

189. Gardella, D., et al.: Differential tissue shrinkage and compression in the z-axis: implications for optical disector counting in vibratome-, plastic-and cryosections. J. Neurosci. Methods. **124** (1), 45–59 (2003) 

190. Nayak, R., Kumar, Venugopal, S.: “Prediction of shrinkage allowance for tool design of aluminium alloy (A356) investment casting.“ Materials Today: Proceedings 5.11 : pp. 24997–25005. (2018) 

191. Oktem, H., Erzurumlu, T.: “Application of Taguchi optimization technique in determining plastic injection molding process parameters for a thin-shell part. Mater. Design. **28** (4), 1271–1278 (2007) 

192. Chen, M.-H., et al.: “Low shrinkage light curable nanocomposite for dental restorative material.“. Dent. Mater. **22** (2), 138–145 (2006) 

193. Hernandez, D.D.: “Factors affecting dimensional precision of consumer 3D printing.“. Int. J. Aviat. Aeronaut. Aerosp. **2** (4), 2 (2015) 

194. Holt, E., Leivo, M.: Cracking risks associated with early age shrinkage. Cem. Concr. Compos. **26** , 521–530 (2004) 

195. Zhang, H., et al.: Soft mechanical metamaterials with unusual swelling behavior and tunable stress-strain curves. Sci. Adv. **4** (6), 8535 (2018) 

196. Correa, D., et al.: “3D-Printed Wood: Programming hygroscopic material transformations.“ 3D Printing and Additive Manufacturing 2.3 : pp.106–116. (2015) 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2888 

197. Abbott, N.J., Goodings, U.A.C.: “14-moisture absorption, density and swelling properties of nylon filaments.“Journal of the Textile Institute Transactions40.4 : pp. (1949). T232-T246. 

198. Dávila, J.L., et al.: Fabrication of PCL/β-TCP scaffolds by 3D mini‐screw extrusion printing. J. Appl. Polym. Sci. **133** , 15 (2016) 

199. Konta, A., Alice, M., García-Piña, Dolores, R., Serrano: “Personalised 3D printed medicines: which techniques and polymers are more successful? " Bioeng. **4** (4), 79 (2017) 

200. Craveiro, F., et al.: “Customizing insulation material properties for building retrofitting: From infrared thermography to additive manufacturing.“ (2018) 

201. Polzin, C., Spath, S., Seitz, H.: “Characterization and evaluation of a PMMA-based 3D printing process.“Rapid Prototyping Journal(2013) 

202. Ćwikła, G., et al.: “The influence of printing parameters on selected mechanical properties of FDM/FFF 3D-printed parts.“ IOP Conf. Ser. Mater. Sci. Eng. Vol. **227** , 1 (2017) 

203. Samykano, M., et al.: “Mechanical property of FDM printed ABS: influence of printing parameters.“. Int. J. Adv. Manuf. Technol. **102** , 9–12 (2019) 

204. Rafai, N.H., Islam, M.N.: An investigation into dimensional accuracy and surface finish achievable in dry turning. Mach. Sci. Technol. **13** (4), 571–589 (2009) 

205. Tiwary, V., Kumar, et al.: “Surface enhancement of FDM patterns to be used in rapid investment casting for making medical implants.“Rapid Prototyping Journal(2019) 

206. Shahrubudin, N., et al.: “Challenges of 3D printing technology for manufacturing biomedical products: A case study of Malaysian manufacturing firms.“ Heliyon 6.4 : p.e03734. (2020) 

207. Nazan, M.A., et al.: “Optimization of warping deformation in open source 3d printer using response surface method.“ Proceedings of Mechanical Engineering Research Day : pp. 71–72. (2016) (2016) 

208. Pei, E., et al.: “Multi-material additive and subtractive prosumer digital fabrication with a free and open-source convertible delta RepRap 3-D printer.“Rapid Prototyping Journal(2015) 

209. Baumann, F., Roller, D.: “Vision based error detection for 3D printing processes.“ MATEC web of conferences. Vol. 59. EDP Sciences, (2016) 

210. Sanatgar, R., Hashemi, C., Campagne, Nierstrasz, V.: Investigation of the adhesion properties of direct 3D printing of polymers and nanocomposites on textiles: Effect of FDM printing process parameters. Appl. Surf. Sci. **403** , 551–563 (2017) 

211. Pilch, Z.: Jarosław Domin, and Andrzej Szłapa. “The impact of vibration of the 3D printer table on the quality of print.“ 2015 Selected Problems of Electrical Engineering and Electronics (WZEE). IEEE (2015) 

212. Spoerk, M., et al.: “Effect of the printing bed temperature on the adhesion of parts produced by fused filament fabrication.“ Plastics. Rubber and Composites. **47** (1), 17–24 (2018) 

213. Meyer, P., Döpke, C., Ehrmann, A.: Improving adhesion of threedimensional printed objects on textile fabrics by polymer coating. J. Eng. Fibers Fabr. **14** , 1558925019895257 (2019) 

214. Tamburrino, F., Graziosi, S., Monica Bordegoni: The influence of slicing parameters on the multi-material adhesion mechanisms of FDM printed parts: an exploratory study. Virtual and Physical Prototyping. **14** (4), 316–332 (2019) 

215. Alsoufi, M.S., et al.: Experimental characterization of the influence of nozzle temperature in FDM 3D printed pure PLA and advanced PLA+. Am. J. Mech. Eng. **7** (2), 45–60 (2019) 

216. Saluja, A., Xie, J., Fayazbakhsh, K.: A closed-loop in-process warping detection system for fused filament fabrication using convolutional neural networks. J. Manuf. Process. **58** , 407–415 (2020) 

217. Alsoufi, M.S., Abdulrhman, E., Elsayed: How surface roughness performance of printed parts manufactured by desktop FDM 3D printer with PLA + is influenced by measuring direction. Am. J. Mech. Eng. **5** (5), 211–222 (2017) 

218. Qattawi, A.: and Muhammad Ali Ablat. “Design consideration for additive manufacturing: fused deposition modelling.“ Open Journal of Applied Sciences 7.6 : pp. 291–318. (2017) 

219. Anderegg, D.A., et al.: In-situ monitoring of polymer flow temperature and pressure in extrusion based additive manufacturing. Additive Manuf. **26** , 76–83 (2019) 

220. Rackers, K.G.: and B. G. Thomas. “Clogging in continuous casting nozzles.“ Steelmaking Conference Proceedings. Vol. 78. IRON AND STEEL SOCIETY OF AIME, (1995) 

221. Tlegenov, Y., Wong, Y.S., Geok Soon Hong: “A dynamic model for nozzle clog monitoring in fused deposition modelling.“Rapid Prototyping Journal(2017) 

222. Ranjan, N., Singh, R., Ahuja, I.P.S.: Development of PLA-HApCS-based biocompatible functional prototype: a case study. J. Thermoplast. Compos. Mater. **33** (3), 305–323 (2020) 

223. Ranjan, N., Singh, R., Ahuja, I.P.S., Kumar, R., Singh, D., Ramniwas, S., Verma, A.K., Mittal, D.: 3D printed scaffolds for tissue engineering applications: Mechanical, morphological, thermal, in-vitro and in-vivo investigations. CIRP J. Manufact. Sci. Technol. **32** , 205–216 (2021) 

224. Kumar, R., Kumar, R.: “3D printing of food materials: A state of art review and future applications.“ Materials Today: Proceedings (2020) 

225. Tlegenov, Y., Wen Feng, L.: Nozzle condition monitoring in 3D printing. Robot. Comput. Integr. Manuf. **54** , 45–55 (2018) 

226. Maloch, J., et al.: “Effect of processing parameters on mechanical properties of 3D printed samples.“ Materials Science Forum. Vol. 919. Trans Tech Publications Ltd, (2018) 

227. Sukindar, N., Aiman, et al.: “Analysis on temperature setting for extruding polylactic acid using open-source 3D printer.“ (2017) 

228. Valino, A.D., et al.: Advances in 3D printing of thermoplastic polymer composites and nanocomposites. Prog. Polym. Sci. **98** , 101162 (2019) 

229. Khan, M., Farhan, A., Alam, M.A., Siddiqui, M.S., Alam, Y., Rafat: Nehal Salik, and Ibrahim Al-Saidan. “Real-time defect detection in 3D printing using machine learning.“ Materials Today: Proceedings 42 : 521–528. (2021) 

230. Baumann, F., Roller, D.: “Vision based error detection for 3D printing processes.“ In MATEC web of conferences, vol. 59, p. 06003. EDP Sciences, (2016) 

231. Miyanaji, H., Momenzadeh, N., Li, Y.: Effect of printing speed on quality of printed parts in Binder Jetting Process. " Additive Manufacturing. **20** , 1–10 (2018) 

232. Hergel, J.: and Sylvain Lefebvre. “Clean color: Improving multifilament 3D prints.“ Computer Graphics Forum. Vol. 33. No. 2. (2014) 

233. Melocchi, A., et al.: 3D printing by fused deposition modeling (FDM) of a swellable/erodible capsular device for oral pulsatile release of drugs. J. Drug Deliv. Sci. Technol. **30** , 360–367 (2015) 

234. Patel, D.M.: “Effects of infill patterns on time, surface roughness and tensile strength in 3D printing.“. Int. J. Eng. Dev. Res. **5** , 566–569 (2017) 

235. Fernandez-Vicente, M., et al.: “Effect of infill parameters on tensile mechanical behavior in desktop 3D printing.“ 3D printing and additive manufacturing 3.3 : pp.183–192. (2016) 

236. Torres, J., et al.: “Mechanical property optimization of FDM PLA in shear with multiple objectives.“ Jom 67.5 : pp.1183–1193. (2015) 

237. Alsoufi, M.S., Abdulrhman, E., Elsayed: Surface roughness quality and dimensional accuracy—a comprehensive analysis of 100% infill printed parts fabricated by a personal/desktop costeffective FDM 3D printer. Mater. Sci. Appl. **9** (1), 11–40 (2018) 

1 3 

International Journal on Interactive Design and Manufacturing (IJIDeM) (2023) 17:2867–2889 

2889 

238. Aliheidari, N., et al.: “The impact of nozzle and bed temperatures on the fracture resistance of FDM printed materials.“ Behavior and Mechanics of Multifunctional Materials and Composites 2017, vol. 10165. International Society for Optics and Photonics (2017) 

239. Rajpurohit, S.R., Harshit, K.: Dave. “Effect of process parameters on tensile strength of FDM printed PLA part.“Rapid Prototyping Journal(2018) 

240. Akhoundi, B., Behravesh, A.H.: “Effect of filling pattern on the tensile and flexural mechanical properties of FDM 3D printed products.“. Exp. Mech. **59** (6), 883–897 (2019) 

241. Wang, P., et al.: Effects of printing parameters of fused deposition modeling on mechanical properties, surface quality, and microstructure of PEEK. J. Mater. Process. Technol. **271** , 62–74 (2019) 

242. Kim, M., Kyung, I.H., Lee, Ho-Chan, K.: “Effect of fabrication parameters on surface roughness of FDM parts.“. Int. J. Precis. Eng. Manuf. **19** (1), 137–142 (2018) 

243. Akhoundi, B., et al.: An Experimental Study of Nozzle Temperature and Heat Treatment (Annealing) Effects on Mechanical Properties of High-Temperature Polylactic Acid in Fused Deposition Modeling. Polym. Eng. Sci. **60** (5), 979–987 (2020) 

244. Alsoufi, M.S., Elsayed, A.E.: Warping deformation of desktop 3D printed parts manufactured by open-source fused deposition modeling (FDM) system. Int. J. Mech. Mechatronics Eng. **17** (4), 7–16 (2017) 

245. Mohamed, O., Ahmed, et al.: Effect of process parameters on dynamic mechanical performance of FDM PC/ABS printed parts through design of experiment. J. Mater. Eng. Perform. **25** , 7 (2016) 

246. Vesely, P.: “Nozzle Temperature effect on 3D printed structure properties.“ (2019) 

247. Calignano, F., Galati, M., Iuliano, L.: “A metal powder bed fusion process in industry: Qualification considerations.“ Machines 7, no. 4 :72. (2019) 

248. Chatham, C.A., Timothy, E., Long: Williams. “A review of the process physics and material screening methods for polymer powder bed fusion additive manufacturing. Prog. Polym. Sci. **93** , 68–95 (2019) 

249. Khorasani, M., Ghasemi, A.H.: Bernard Rolfe, and Ian Gibson. “Additive manufacturing a powerful tool for the aerospace industry.“Rapid prototyping journal(2021) 

250. Babbar, A., Sharma, A., Jain, V., Gupta, D. (eds.): Additive Manufacturing Processes in Biomedical Engineering: Advanced Fabrication Methods and Rapid Tooling Techniques, p. 29. CRC Press (2022 Jul) 

251. Kalia, G., Sharma, A., Babbar, A.: Use of three-dimensional printing techniques for developing biodegradable applications: A review investigation. Materials Today: Proceedings. Apr 2. (2022) 

252. Babbar, A., Rai, A., Sharma, A.: Latest trend in building construction: three-dimensional printing. InJournal of Physics: Conference Series 2021 Aug 1 (Vol. 1950, No. 1, p. 012007). IOP Publishing 

253. Babbar, A., Sharma, A., Kumar, R., Pundir, P., Dhiman, V.: Functionalized biomaterials for 3D printing: An overview of the literature. Additive Manuf. Functionalized Nanomaterials. **1** , 87–107 (2021 Jan) 

254. Babbar, A., Jain, V., Gupta, D., Prakash, C., Singh, S., Sharma, A.: 3D bioprinting in pharmaceuticals, medicine, and tissue engineering applications. InAdvanced Manufacturing and Processing Technology 2020 Oct 25 (pp.147–161).CRC Press 

255. Singh, D., Babbar, A., Jain, V., Gupta, D., Saxena, S., Dwibedi, V.: Synthesis, characterization, and bioactivity investigation of biomimetic biodegradable PLA scaffold fabricated by fused filament fabrication process. J. Brazilian Soc. Mech. Sci. Eng. **41** (3), 1–13 (2019) 

256. Babbar, A., Jain, V., Gupta, D., Sharma, A., Prakash, C., Kumar, V., Goyal, K.K.: Additive Manufacturing for the Development of Biological Implants, Scaffolds, and Prosthetics. InAdditive Manufacturing Processes in Biomedical Engineering (pp.27–46).CRC Press 

257. Kumar, V., Prakash, C., Babbar, A., Choudhary, S., Sharma, A., Uppal, A.S.: Additive Manufacturing in Biomedical Engineering: Present and Future Applications. InAdditive Manufacturing Processes in Biomedical Engineering (pp.143–164).CRC Press 

**Publisher’s Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Springer Nature or its licensor holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law. 

1 3 

