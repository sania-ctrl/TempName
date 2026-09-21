**_polymers_** 





_Review_ 

# **Fused Filament Fabrication Process: A Review of Numerical Simulation Techniques** 

**Ans Al Rashid**<sup>**1,**</sup> *** and Muammer Koç**<sup>**1,2**</sup> 

- 1 Division of Sustainable Development, College of Science and Engineering, Hamad Bin Khalifa University, Qatar Foundation, Doha 34110, Qatar; mkoc@hbku.edu.qa 

- 2 Faculty of Engineering, University of Karabük, Karabük 78050, Turkey 

- Correspondence: anrashid@hbku.edu.qa 

��������� **�������** 

**Citation:** Rashid, A.A.; Koç, M. Fused Filament Fabrication Process: A Review of Numerical Simulation Techniques. _Polymers_ **2021** , _13_ , 3534. https://doi.org/10.3390/ polym13203534 

**Abstract:** Three-dimensional printing (3DP), also known as additive manufacturing (AM), has rapidly evolved over the past few decades. Researchers around the globe have been putting their efforts into AM processes improvement and materials development. One of the most widely used extrusion-based technology under AM processes is Fused Deposition Modeling (FDM), also known as Fused Filament Fabrication (FFF). Numerical simulation tools are being employed to predict the FFF process complexities and material behavior. These tools allow exploring candidate materials for their potential use in the FFF process and process improvements. The prime objective of this study is to provide a comprehensive review of state-of-the-art scientific achievements in numerical simulations of the FFF process for polymers and their composites. The first section presents an indepth discussion of the FFF process’s physical phenomena and highlights the multi-level complexity. The subsequent section discusses the research efforts, specifically on numerical simulation techniques reported in the literature for simulation of the FFF process. Finally, conclusions are drawn based on the reviewed literature, and future research directions are identified. 

**Keywords:** additive manufacturing; 3D printing; computational modeling; simulation technique; computational fluid dynamics 

## **1. Introduction** 

Academic Editors: Yancheng Wang and Roland Kuen Ren Chen 

Received: 4 September 2021 Accepted: 1 October 2021 Published: 14 October 2021 

**Publisher’s Note:** MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations. 



**Copyright:** © 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/). 

Three-dimensional printing, also known as additive manufacturing (AM), has rapidly evolved over the past few decades [1,2]. AM processes allow the fabrication of threedimensional and functional components through successive additions of 2D layers [3]. AM was first introduced by Hull [3], since then, researchers have established several process technologies and novel materials [4]. These processes have attracted the research interest due to higher flexibility in the design and the manufacturing of highly customizable parts, rapid prototyping of conceptual products, waste reduction, lower risk of human error, and higher precision and accuracy than conventional manufacturing processes [5–7]. AM processes are now being widely adopted in several industrial sectors owing to these advantages [8,9]. 

Fused Deposition Modeling (FDM), also known as Fused Filament Fabrication (FFF), one of the most widely used AM processes, was proposed and developed by Scott Crump at Stratasys [10]. In the FFF process, the material is supplied to the 3D printer in the form of filaments. The extruder in any FFF-based 3D printer generally contains a feed material control mechanism, heating chamber, and nozzle. The material in the filaments form is fed to the control system, which controls the feed rate. Then the filament moves through the heating chamber, which converts it into a semi-solid phase and then passes through the nozzle for deposition on the printing bed [11]. The mechanical and thermal controls in the extruder govern the overall printing process and depend upon the feed-stock material properties. Thermoplastics, particles reinforced polymers, and hydrogels have been fabricated using the FFF process [12]. 

_Polymers_ **2021** , _13_ , 3534. https://doi.org/10.3390/polym13203534 

https://www.mdpi.com/journal/polymers 

_Polymers_ **2021** , _13_ , 3534 

2 of 20 

Researchers around the globe have been putting their efforts into AM processes improvement and novel materials over the past few decades [13,14]. The research efforts include process printing speed, printer build volume, and production rate [15]. The materials portfolio has also included short and continuous fiber-reinforced polymer composites for the FFF process [16–18]. Aside from the extensive experimental investigations on the FFF process reported in the literature, the numerical tools employed are still limited. 

The prime objective of this study is to provide a comprehensive review of the state-ofthe-art scientific achievements in numerical simulations of the FFF process for polymers and their composites. The first section presents an in-depth discussion of the FFF process’s physical phenomena and highlights the multi-level complexity. The subsequent section discusses the research efforts, specifically on numerical simulation methods reported in the literature for simulation of the FFF process. Finally, conclusions are drawn based on the reviewed literature, and future research directions are identified. 

## **2. Physics Involved in Fused Filament Fabrication Process** 

This section presents the physical phenomena involved in the FFF process. An indepth understanding of this phenomenon is essential to improve the process and 3D printed part quality. The overall FFF process can be divided into three phases; material flow through the nozzle and deposition on the print bed or already deposited material (extrusion), interaction of deposited beads to make a bond (fusion), and the cooling process (solidification), as elaborated in Figure 1. 

The first process involves material flow through the nozzle body, nozzle orifice, and deposition [19]. This phase is of great interest, especially in the 3DP of fiber-reinforced polymer composites, as fiber orientation results from material flow through the orifice and regulates mechanical behavior (anisotropy) of the fabricated part. The flow behavior and fiber orientation are interdependent, as a viscous fiber-suspension flow is obtained for materials with considerable fiber volume fractions. Shear alignment phenomena and converging zone in nozzle determine the fiber orientation in printed beads. The viscosity of the material is also dependent upon fiber orientation. For example, the extensional viscosity parallel to fiber alignment is multiple folds higher than in the transverse direction. 



<!-- Start of picture text -->
Flow and fiber orientation:<br>Solidification behavior: * Viscous suspension flow<br>stool down "Flow andfiber orientation<br>* Viscoelastic behavior mutually dependent<br>* Gravity effects Material Flow<br>= Crystallization kinetics<br>= Shrinkage Bond formation: Die<br>* Residual stresses * Fiber affect surface NY,<br>tensions and necking Cy<br>* Effect of crystallization )<br>—><br>Relative Movement<br>j<br>Deposited Material<br>Printing Bed<br><!-- End of picture text -->

**Figure 1.** Schematic diagram of the FFF process. Reprinted with permission from reference [20]. Copyright 2018, Elsevier. 

_Polymers_ **2021** , _13_ , 3534 

3 of 20 

In the second phase, the deposited material reheats or re-melts the already deposited material beads [21]. The bonding between the extruded filaments is highly dependent on this wetting phenomenon [22]. The wetting phenomena regulate the contact area between the deposited filaments, as prolonged interface exposure at elevated temperatures assists the merging of adjacent beads and polymer chains diffusion [23]. The viscosity of beads in the transverse direction and surface tension of the material controls this wetting process. A limited temperature range is available for perfect bead formation between the layers, as viscosity is temperature-dependent [24]. Diffusion-based fusion is observed between the beads at higher temperatures after an interface has been formed. However, the diffusion process is obstructed due to reduced molecular mobility at lower temperatures. Therefore, a critical factor for adequate bonding is the temperature history of printed material. Additional complexity arises for semi-crystalline materials, as the viscosity of such materials rapidly increases at crystallization temperature, interrupting the bond formation process [25]. 

Lastly, the deposited material begins to solidify as it cools down. The cooling process during and post-printing is governed by convective and radiative heat losses on external surfaces of the beads and conductive heat transfer at beads contact points and printing bed. If the material is deposited at a higher speed, i.e., a large amount of material is deposited in a shorter time, it will not allow the pre-laid layer to cool down sufficiently before depositing the next layer [26]. It will result in sagging due to gravity and print failure. The material converts to a viscoelastic solid from a viscous fluid during the cooling process and starts shrinking depending upon the coefficient of thermal expansion (CTE). The internal stresses begin to develop due to material stiffness produced by the solidification process and restriction due to bead fusion. Viscoelastic relaxation and material deformations assist a fraction of internal stresses to be released. However, for semi-crystalline polymers, the mechanical and thermal properties change during the crystallization process. For such materials, additional strains are observed that further cause internal stresses and part deformations, resulting in altered mechanical properties [27]. The presence of fibers aligned in the printing direction also affects the thermal properties due to increased thermal conductivity. Thermomechanical and crystallization effects constraints the shrinkage process in the bead direction, but not to the same degree in the lateral direction [28]. The physical phenomena involved in the FFF process highlight its complexity. Therefore, the above-discussed process physics and interactions must be considered for more realistic process simulation and modeling. 

## **3. Numerical Simulation Techniques** 

There has been an increasing interest in modeling and simulation of the FFF process since the commercial availability of 3D printers. The past and ongoing research related to computational modeling of the FFF process can be broken down into two domains. In the first domain, thermal variations and fluid flow behavior of the material in the heating zone are modeled. Overall melt flow behavior of the material inside the printer extruder depends upon the heat capacities of the nozzle and liquefier and the thermal properties of the material. Secondly, when the material is extruded through the nozzle, sudden pressure change causes swelling following the deposition. This stage is of great interest as material flow outside the nozzle, bead shape, bonding of beads, and residual stresses are governed by these factors. Following, we present the computational works related to the FFF of polymers and polymer composites, also reported in Table 1. 

_Polymers_ **2021** , _13_ , 3534 

4 of 20 

**Table 1.** Summary of studies reported on the numerical modeling of fused filament fabrication process. 

|**Material**|**Additives**|**Analysis**|**Tools**|**Highlights**|**Ref.**|
|---|---|---|---|---|---|
|PCL|-|Melt Flow<br>Behavior|ANSYS©|Observation of velocity, pressure, and thermal<br>variations.<br>Filament velocity at the inlet of the channel<br>was varied.<br>Variation in nozzle shape and the angle at<br>the exit.<br>Material liquified within 35% of the<br>channel length.|[29]|
|ABS|Iron Particles<br>(10%)|Melt Flow<br>Behavior|ANSYS©|Study of velocity, temperature, and pressure<br>variations.<br>Fabrication and characterization of composites.<br>Promising simulation results for melt flow<br>behavior and process optimization.|[30]|
|||||Potential for using fine nozzle diameters for<br>MAFD.||
|ABS|-|Swelling and<br>Filament<br>Cooling|Dieplast© and<br>EFD Lab|Nozzle temperature regarded as primary<br>contributor to die swelling.<br>Temperature variations along the nozzle length.<br>Volume of flow 215 times lower than<br>conventional nozzles.|[31]|
|ABS|-|Melting Inside<br>Nozzle|Mathematical<br>Model|Analytical model for melting inside the nozzle.<br>Material flow was controlled by applied force.<br>Experimental validation of proposed model.<br>Good prediction of material behavior for force<br>up to 40 N.|[32]|
|||||Simple model for warpage deformation was<br>developed.||
|ABS|-|Warpage|Mathematical<br>Model|All influencing parameters (layer number,<br>chamber temperature, material shrinkage rate)<br>were quantitatively analyzed.<br>Recommendations to avoid warp deformation.|[33]|
|||||Analytical model based on experimental<br>observations was developed.||
|ABS|-|Warpage|Mathematical<br>Model|<br>Model can predict multi-layer deformation of<br>3D printed parts.<br>Strong effect of layer thickness on warpage<br>was observed.|[34]|
|ABS|CF|Fiber<br>Orientation|COMSOL©<br>MATLAB©|Effect of nozzle geometry and extrudate swell.<br>Used Floger-Tucker [35] and Advani and<br>Tucker [36] models.<br>Comparable results to previously reported<br>studies [37,38].|[39]|
|ABS|CF|Fiber<br>Orientation|SPH-DEM|Both short and continuous fiber composites.<br>Highly aligned short fibers with material flow<br>over time.<br>Lower printing speeds recommended for<br>continuous fiber composites to avoid nozzle<br>wear and fiber breakage.|[40]|
|ABS|-|Solidification|ANSYS©|Rectangular cross-section of deposited beads.<br>3D model to investigate thermal behavior.<br>Similar stepwise activation, as reported by [41].<br>Thermal properties of the material were found<br>to have a significant effect on the<br>solidification process.|[42]|



_Polymers_ **2021** , _13_ , 3534 

5 of 20 

**Table 1.** _Cont._ 

|**Material**|**Additives**|**Analysis**|**Tools**|**Highlights**|**Ref.**|
|---|---|---|---|---|---|
|ABS|-|Solidification|Mathematical<br>Model|Both convective and radiative heat transfer<br>phenomena were considered to develop a<br>3D model.<br>The numerical model results found sound<br>agreement with experimental results.|[43]|
|||||First model to predict the bond<br>formation mechanism.||
|ABS|-|Bond<br>Formation|Mathematical<br>Model|1D lumped heat transfer model was used.<br>The model also considered the effect of<br>printing parameters.<br>Concluded better control of the cooling process<br>to control mechanical properties of FFF parts.|[44]|
|PLA|-|Melt Flow<br>Behavior|ANSYS©|Experimentally obtained liquefier temperature<br>profile and heating element power output.<br>Detailed 3D model with all assemblies.<br>External heat transfer mechanisms were found<br>more significant.|[45]|
|||||Rheological and mechanical properties<br>obtained experimentally.||
|PLA|CNF<br>(0–1%)|Melt Flow<br>Behavior|ANSYS©|<br>Simulation of non-Newtonian fluid flow using<br>3D model.<br>Results agreed well with existing<br>numerical models.|[46]|
|PLA|-|Warpage|Mathematical<br>Model<br>Statistical Analysis|2D analytical model based on theory of thin<br>plates.<br>Taguchi’s method was used for design of<br>experiments.<br>ANOVA and S/N ratio were used to optimize<br>the process parameters.<br>Proposed model was found efficient but<br>thermal stresses were ignored.|[47]|
|PLA|-|Warpage|Mathematical<br>Model|Successful prediction of distortion for PLA<br>thin walls.<br>Limitation in terms of warpage magnitude.|[48]|
|PLA|-|Bead<br>Deposition and<br>Solidification|Mathematical<br>Model|A model for viscoelastic materials<br>The front-tracking/finite volume method<br>was used.<br>Three extruded filaments built vertically were<br>simulated considering viscoelastic stresses.<br>The model was also employed to larger objects.|[49]|
|||||Nozzle equipped with pressure and<br>temerature sensors||
|ABS,<br>PCL,<br>PLA|-|Swelling and<br>Process<br>Conditions|SolidWorks©|p .<br>High shear rates resulted in a higher swell.<br>Viscosity models were obtained from<br>experimental analysis.<br>Simulations agreed well with experimental<br>data.|[50]|
|PP|-|Melt Flow<br>Bead Shape<br>Residual<br>Stresses<br>Warpage|ANSYS©|Experimental and numerical investigation.<br>Special focus on warpage and<br>mechanical properties.<br>Good agreement of numerical simulation<br>results with experimental observations.|[51]|



_Polymers_ **2021** , _13_ , 3534 

6 of 20 

**Table 1.** _Cont._ 

|**Material**|**Additives**|**Analysis**|**Tools**|**Highlights**|**Ref.**|
|---|---|---|---|---|---|
|PPS|AIN|Warpage|ANSYS©|Extended work from Watanable [51].<br>Analysis of most significant material parameter.<br>CTE concluded most significant for<br>part warpage.<br>Composite materials with lower CTE can<br>reduce warpage.|[28]|
|PPS|CF|Solidification<br>Crystallization|COMSOL©|2D model for thermal history and<br>crystallization behavior.<br>Used non-isothermal dual crystallization<br>kinetics model.<br>Individual activation of beads.<br>Thermal variations of the beads in the printing<br>direction were not considered.|[41]|
|Photo<br>Poly-<br>mer|AgNWs<br>(1.6 vol%)|Nanofiller<br>orientation|ANSYS©|Nozzle geometry effect on fiber orientation.<br>Aligned nanowires for circular nozzle.<br>Different velocity profiles at nozzle exits.|[52]|
|||||Melt flow within the nozzle.||
|Epoxy|CF<br>(8 vol%)|Fiber<br>Orientation|STARCCM+|Fibers interactions with other fibers, epoxy,<br>and wall.<br>Higher fiber orientation near to the wall.|[53]|



## _3.1. Melt Flow Behavior_ 

The first study on modeling and characterization of material flow inside the liquefier and nozzle in the FFF process was conducted by Bellini [54]. The material flow through the FFF extrusion system (i.e., liquefier, nozzle, and die) for ceramic materials were modeled and discussed for PZT/ECG9 material. The pertinent achievement of this study included a tool for the controlled deposition process. A model was developed for the selection of the optimal nozzle shape from extensive experimental results. The velocity and temperature fields of the material during the deposition process were simulated and compared with experimental results. Moreover, the incorporated particles were observed to be aligned in the printing direction of extruded strands, but this effect was not included in simulations. 

Although the first study in this area considered ceramic materials, it laid the foundation for the numerical analysis of 3D printed polymers. Ramanath et al. [29] numerically investigated the melt flow behavior of Poly-ε-caprolactone (PCL) biomaterial processed via the FFF process. PCL is an emerging material in the biomedical field, as it has found its applications in this sector due to its biodegradability [55]. An accurate channel model was employed to study the velocity gradient, pressure variations, and thermal behavior by varying filament velocity at entry and nozzle shape and the angle at the exit. From mathematical and numerical results, velocity profiles and pressure gradients strongly depended on the flow channel parameters. Temperature profiles revealed that material completely liquefied within 35% of the channel length, which is an important outcome and can be implemented to predict the melt flow behavior of other materials. Researchers have also considered ABS material for numerical studies. ABS material can is widely regarded for the synthesis of polymer composites [56]. This material has found its mechanical applications due to its impressive mechanical and physical properties and chemical resistance [57,58]. Monzón et al. [31] conducted a theoretical and experimental study to evaluate the potential of using a 0.05 mm diameter nozzle for the FFF process. The material swelling and filament cooling during the deposition process was studied for ABS. A conventional FFF printer was used to extrapolate the information for micro-additive fused deposition (MAFD). Die swelling was attributed to nozzle and envelope temperature, where nozzle temperature plays a more significant role. In addition, due to the location of the heating element, temperature variations were observed along the nozzle length with 

_Polymers_ **2021** , _13_ , 3534 

7 of 20 

the lower temperature at the nozzle exit. The nozzle diameter and extrudate diameter ratio were used for the proposed extrapolation and termed the swelling diameter factor. It was concluded that the flow volume could be reduced multiple folds using fine nozzle diameters (i.e., up to 215 times). 

In another study, Bellini et al. [59] studied the response of the extrusion system that was analyzed to design a control system for controlling the material flow. A dynamic system model was developed from a derived analytical model to study the system response based on a defined input. The results from this model were compared with experimental data for ABS material. Steady-state error in the dynamic model was observed due to slippage between filament and extruder rollers. In addition, the limitation in the motor torque and power and temperature variation in the liquefier was identified as the reason for the time-delay in response. Likewise, the most appropriate operating temperatures and shear rates for MAFD were explored by Ortega et al. [50]. The analyses were performed on acrylonitrile butadiene styrene (ABS), polylactic acid (PLA), polycaprolactone (PCL), and poly (vinyl alcohol) (PVA). A MAFD nozzle (300 µm) was used to obtain the viscosity models used in the simulation of materials under different operating conditions. The simulation results agreed well with the experimental data. Osswald et al. [32] proposed an analytical model for material melting inside the nozzle, where the applied force governed the maximum melting rate. The model included effects of initial filament temperatures, heater temperature, applied force, nozzle tip angle, capillary diameter, length, and rheological and thermal properties. Experiments performed on ABS material were used to validate the analytical model (Figure 2), and it was concluded that the model accurately predicts melting behavior for forces up to 40 N. 



<!-- Start of picture text -->
“ F<br>.<br>a<br>5 as |<br>Weight | Piston By -U..<br>Movable platform Ps<br>~ 7 “PTFE insert<br>| rr =<br>| - Polymer filament<br>Linear bearings<br>mane = |<br>—<br>~Q (polymer met flow rate)<br><!-- End of picture text -->

**Figure 2.** Experimental setup used for validation of the analytical model. Reprinted with permission from reference [32]. Copyright 2018, Elsevier. 

_Polymers_ **2021** , _13_ , 3534 

8 of 20 

Other than PCL and ABS, Polylactic acid (PLA) is also a widely explored polymer in materials science due to its sustainability and biodegradability [60]. PLA is also an FDAapproved biocompatible material used in medical and food packaging applications [61,62]. Stewart et al. [45] numerically and experimentally investigated the melt flow behavior of the PLA material in the FFF process. The power output of the heating element and temperature profiles within the liquefier were recorded experimentally. The material properties and initial conditions calculated from experimental data were used for 3D modeling of the fluid flow using an accurate extruder geometry. The simulation results concluded that external convective and radiative heat losses play a significant role in material flow realistically. 

## _3.2. Fiber Orientation in Polymer Composites_ 

Numerical studies on fused filament fabrication of fiber-reinforced materials are limited. Fiber orientation during the FFF process and mechanical properties are strongly affected by nozzle shape, fiber concentration, material flow rate, and pressure difference. The use of computational modeling software, such as ANSYS<sup>®</sup> , COMSOL<sup>®</sup> , and Moldflow<sup>®</sup> , is reported in the literature. Mostafa et al. [30] investigated the melt flow behavior of iron particle-reinforced Acrylonitrile butadiene styrene (ABS) composites. Twoand three-dimensional numerical simulations were performed using computational fluid dynamics (CFD) software to analyze the temperature, pressure, and velocity changes. Both techniques provided a good correlation in predicting the melt flow behavior. Finally, ABS-iron particle composites were produced and processed to fabricate the samples. Papon et al. [46] studied the effect of FFF process parameters on the melt flow behavior of carbon nanofiber (CNF)-reinforced PLA nanocomposites. A numerical model for non-Newtonian flow was developed to investigate the effect of material properties and different nozzle geometries. Experiments were performed to identify the material rheological properties, and a 3D model of the FFF extrusion channel was developed for simulation. Temperature, pressure, and velocity profiles were obtained, compared with the existing literature, and provided sound agreement. 

Fiber orientation in short or continuous fiber-reinforced composites is critical to achieving desired mechanical, thermal, or electrical properties in 3D printed materials. Several experimental studies provided insight into fiber orientation and fiber flow behavior within the nozzle and deposition of extruded beads [63–66]. However, reported work related to numerical studies will be focused here; readers are referred to the mentioned literature for more details on experimental studies. Kim et al. [52] synthesized silver nanowire (AgNWs)-reinforced photopolymer composites and investigated the effect of nozzle geometry on nanoparticles orientation. Nanocomposites revealed higher dielectric permittivity when 3D printed using a circular nozzle than the flat nozzle, owing to aligned nanowires in the printing direction. Different velocity profiles at nozzle exits obtained from numerical simulations also evidenced the orientation of the nanowires along with the fluid flow for a circular nozzle. 

Heller et al. [39] studied the effect of nozzle geometry and extrudate swell on fiber orientation of carbon fiber (CF)-reinforced ABS composites. The numerical model was developed in COMSOL integrated with a MATLAB interface. An incompressible fluid flow was modeled considering a Newtonian fluid melt. Fiber orientation was explained using Floger-Tucker [35] and Advani and Tucker [36] models for orientation and isotropic rotary diffusion, respectively. The obtained results were comparable to previously reported studies [37,38]. The authors also performed a parametric analysis to optimize the nozzle geometry for the best achievable modulus in the printing direction. Lewicki et al. [53] performed numerical simulation for CF-reinforced epoxy composites to investigate the melt flow behavior and fiber orientation during the extrusion process. The fibers’ interactions with other fibers, epoxy, and wall were also considered. Randomly oriented fibers were considered at the start, and fiber alignment during the flow was modeled, as shown in Figure 3. The wall-dominated shear alignment was observed from simulation results, resulting in higher fiber orientation along with the flow near to the wall. 

_Polymers_ **2021** , _13_ , 3534 

9 of 20 



<!-- Start of picture text -->
Se MAX aE Ee :<br>< ><br>far<br>“ “eee Se a = on<br>« \ pa eget Ve ZN \<br>ES ea. [== D<br>eeRTE FATT ETaeEe aePO AeTE TTTa TOSI<br>P 30.20 a Sara yee Vee =<br>0.10 - Zs EE Se =<br>C ‘0.00| ————=<br>/ SSO Oo<br>020 -0.10 000 0.10 0% : a =<br>a,<br>=<br><!-- End of picture text -->

**Figure 3.** ( **A** ) Presents the simulations domain considered for analysis. ( **B** , **C** ) Shows the side views of the extrusion head with random fiber orientations. ( **D** ) Snapshots of the simulation presenting the fiber flow. Reprinted with permission from reference [53]. Copyright 2017, Science Direct. 

In addition to the numerical simulations of fiber-reinforced material flow within the nozzle, several studies have reported the fiber orientation within the deposited beads. Bertevas et al. [67] were the first ones to model fiber orientation of 3D printed beads. A Smoothed Particle Hydrodynamics (SPH) framework was employed using a microstructurebased model. The fiber orientation prediction near the nozzle complemented the results from Lewicki et al. [53]. However, it was concluded that fiber orientation near the nozzle should not be approximated as the expected fiber orientation of deposited beads due to significant variations in orientations during deposition. The 3DP process parameters were also identified as critical in fiber orientation within the beads. Yang et al. [40] reported an SPH and discrete element method (DEM) approach to model fiber orientation of short and continuous fiber-reinforced composites. The fiber orientation simulation results for discontinuous fiber composites agreed well with Bertevas et al. [67] observations. The short fibers aligned with the flow direction over time and were supported by the literature, whereas continuous fibers experienced high bending deformations and contact with the nozzle (Figure 4). 

_Polymers_ **2021** , _13_ , 3534 

10 of 20 



<!-- Start of picture text -->
t=0.05s «10 m/s t=01s<br>1.80<br>5 2.01.6 0<br>= 1.40<br>1.00<br>5 1.20<br>4.00<br>2.00<br>6 |.0.00<br>- t=0.05s 10" m/s t=O01s<br>3 e 2<br>Es 1.60<br>q ‘3<br>1.00<br>8.00<br>6.00<br>4.00<br>2.00<br>z 0.00<br>ix<br><!-- End of picture text -->

**Figure 4.** Velocity profiles for short and continuous fiber-reinforced composites. Reprinted with permission from reference [40], Copyright 2017, MDPI. 

## _3.3. Solidification Behavior_ 

The solidification behavior of material governs the bonding between deposited beads, polymer crystallization, and ultimately the mechanical properties of the 3D printed part. When two adjacent beads are deposited, they contact and form necking at the interface [68] (Figure 5). The resulting mechanical properties of 3D printed parts depend upon process parameters and type of polymer. In this section, the numerical and analytical studies related to solidification behavior are presented. Yardimci et al. [69] were the first to model the deposited beads bonding and their thermal interaction with surroundings. A one-dimensional heat transfer model was used, considering beads as grid blocks. Beads surfaces were modeled under convective conditions. Peclet and Biot’s numbers were identified as significant parameters for thermal distributions. Brenken et al. [41] reported a 2D model for CF-reinforced PPS composites’ thermal history and crystallization behavior. A non-isothermal dual crystallization kinetics model was employed to predict crystallization during the solidification process, where beads were individually activated. This model did not consider the thermal variations of the beads in the printing direction. Figure 6 shows the crystallinity distribution of two adjacently deposited beads. 

_Polymers_ **2021** , _13_ , 3534 

11 of 20 



<!-- Start of picture text -->
2a, Dy 2a<br>NA)ot (AXEae GREEN=a ees<br>Wi Be ls SaaS SLaiat=p,<br>(ly (2) Q)<br><!-- End of picture text -->

**Figure 5.** Bead–bead interaction and bond formation mechanism. ( **1** ) Contact between deposited beads. ( **2** ) Neck formation. ( **3** ) Polymer chains diffusion. Reprinted with permission from reference [44]. Copyright 2004, Elsevier. 



<!-- Start of picture text -->
Time=30 s Surface: Relative crystallinity Bead 1-3<br>4s 40.23<br>4<br>0.2<br>3.5<br>° 4<br>25<br>01s<br>2<br>Ls<br>or<br>1<br>os<br>0<br>0.05<br>0.5<br>a<br>15 vi.74x108<br>as o1 05 0 08 1 1S 200 258 35 4 45<br><!-- End of picture text -->

**Figure 6.** Modeled crystallinity distribution during a print simulation of a simple 2 by 2 bead cross section. Beads 1–3 are active (deposited), while bead 4 is still inactive. Reproduced with permission from reference [20]. Copyright 2018, Elsevier. 

_Polymers_ **2021** , _13_ , 3534 

12 of 20 

Zhou et al. [42] considered a rectangular cross-section of deposited beads and developed a 3D model to investigate the thermal behavior of ABS material using ANSYS©. A similar methodology of step-wise activation, reported by [41], was used for modeling. The thermal properties of the material were found to have a significant effect on the solidification process. In another study, both convective and radiative heat transfer phenomena were considered to develop a 3D analytical model [43]. The numerical model results found sound agreement with experimental. 

Xia et al. [49] recently presented a bead deposition and solidification model for viscoelastic materials, similar to Liu et al. [70]. The FFF process was modeled using the front-tracking/finite volume method. Three extruded filaments built vertically were simulated considering viscoelastic stresses, and the model was also employed to larger objects (Figure 7). Bellehumeur et al. [44] were the first to predict the bond formation mechanism in 3D printed ABS analytically. A 1D lumped heat transfer model was used to predict the thermal variations. The following governing ordinary differential equation was used: 





<!-- Start of picture text -->
Temperature [°C]<br>20.0 36.3 52.5 68.8 85.0 101 118 134 150 166 183 199 215<br>ee<br>(a) (b) (c)<br>(da) (e) i)<br>(g) S (hy . (i) -<br><!-- End of picture text -->

**Figure 7.** Temperature profiles for simulated printed beads in multi-layer deposition. ( **a** – **i** ) frames in time order, from the simulation of printing three filaments in parallel. Reprinted with permission from reference [49]. Copyright 2019, ESLEVEIR. 

The above equation was solved analytically with defined boundary conditions to obtain the following solution for temperature variations during the cooling process: 



Subsequently, sintering experiments were performed to investigate the dynamics involved in the bond formation of extruded filaments. The developed model also considered the effect of different printing parameters. It was suggested that better control 

_Polymers_ **2021** , _13_ , 3534 

13 of 20 

of the cooling process could assist in controlling the mechanical properties of FFF parts. Further investigation was conducted in another study [71], where a non-isothermal model was used to predict the bonding phenomena. This model was highly sensitive to time and temperature variations. Sun et al. [72] experimentally and numerically investigated the mechanism involved in controlling the bond formation. Sintering temperature had a significant effect on the bond formation and, ultimately, the strength. These observations were also complemented in another work [73]. Costa et al. [74,75] reported a model to consider transient heat transfer during material deposition. Bead–bead, bead–platform, and bead–environment contacts were considered in this model. A MATLAB© code was developed to predict the thermal response and beads adhesion from deposition to complete solidification. Mcllroy et al. [76,77] thoroughly investigated the polymer chains’ effect on crystallization behavior. The models included Rolie-Poly formulas to account for polymer chains diffusion and the impact of shear rate on chains diffusivity, degree of crystallization, and bead–bead chains diffusion. 

## _3.4. Residual Stresses and Warpage_ 

The strength and dimensional stability of 3D printed parts are affected by induced residual stresses and warpage. Wang et al. [33] developed a simple analytical model after rigorous simplifications to predict the warp deformation after the FFF process in ABS and quantitatively analyzed all the influencing factors. The following expression was derived to predict the inter-layer warpage ( _δ_ ): 



where _R_ corresponds to the radius of curvature, _L_ represents the section length of the part, _n_ presents the number of deposited layers, ∆ _h_ corresponds to single-layer thickness, and _Tg_ and _Te_ represent glass-transition and chamber temperatures. Based on the model analysis, some recommendations were made to reduce the warpage phenomena effectively. Likewise, Armillotta et al. [34] 3D printed ABS samples with varying process parameters and observed wrap deformation for each case. Statistical tools were employed to identify the optimum parameters. The deflection in the 3D printed specimens due to warpage ( _δT_ ) was calculated using the following expression: 



An analytical model was also derived for both the elastic and plastic behavior of multiple-layer deformations based on the experimental observations. Layer thickness significantly affected the residual stresses, warpage, and surface characteristics. 

Xinhua et al. [47] developed a mathematical model for the warpage mechanism in a thin plate of PLA material based on the elastic theory of thin plates. A special part was 3D printed and analyzed by statistical methods to validate the analytical model. Statistical methods were found beneficial to optimize the process parameters, and the proposed model also provided efficient results. However, this model was also based on assumptions, as beads were assumed to be deposited at once, and thermal stresses were neglected. Wijnen et al. [48] replaced the temperature step-function in the model presented by Wang et al. [33] with a physics-based temperature gradient. The proposed model was successfully applied to predict the warpage in thin walls of PLA; however, the limitation of this model was predicting the magnitude of the warpage. 

_Polymers_ **2021** , _13_ , 3534 

14 of 20 

Watanable [51], using a similar 2D model proposed by Bellini [54], performed an extensive study on polypropylene to predict temperature profiles, deposited bead shapes, residual stresses, and warpage deformations. The study was extended to investigate the warpage in PP, and it was suggested to implement PP composites for warpage reduction. The proposed model can be used to simulate novel materials for exploration and applications in the FFF process. 

Fitzharris et al. [28] extended the work reported by Watanable [51] to investigate the warpage of high-performance polymer, PPS. Part warpage deformations were obtained experimentally compared to PP results (from Watanable [51]). Material parameters for PPS (including coefficient of thermal expansion CTE, thermal conductivity, heat capacity, and young’s modulus) were individually adjusted to PP values to understand their effect on part warpage. CTE was regarded as the most significant parameter governing the part warpage, residual stresses, and shrinkage from simulation results. In addition, simulation was performed considering material parameters for aluminum nitride (AIN)-filler-reinforced PPS. The incorporation of fillers can alter the CTE, increase thermal conductivity and young’s modulus of PPS. The simulation results for PPS/AIN composite resulted in reduced part warpage. 

Zhang and Chou [78] presented a 3-dimensional FEA model for distortion analysis in FFF printed parts. Radiation and conduction heat transfer phenomena were considered in the model, and residual stresses were analyzed using ANSYS©. However, the model lacked the beads interaction during solidification. The sensitivity of residual stresses on process parameters was also studied, and printing speed was identified as an essential parameter in residual stresses. Xia et al. [79] built a more realistic FFF simulation upon their initial work on melt flow [80]. The model was also able to predict the part deformations and material shrinkage over time. The high thermal variations can result in residual stresses; however, this model did not consider the printing bed temperature. In addition to these studies, the same authors also analyzed the shapes of the deposited beads [80]. 

Cattenone et al. [81] developed a framework for 3D simulations on 3D printed parts deformation using ABAQUS©. The mechanical properties were analyzed by varying timestep and mesh, and the results agreed with experimental observations. But this model did not account for bead–bead and bead–print bed interactions. Favaloro et al. [82] were the first to present residual stresses and warpage analysis on polymer composites. ABAQUS© was used to simulate PPS/CF composites using the progressive element activation reported in another work [41]. The model was able to predict the deformations due to crystallization, residual stresses, and part removal. Figure 8 presents the simulation results of residual stresses induced in the 3D printed part after cooling. 

Talagani et al. [83] explored the potential use of numerical tools to simulate a full-scale car model. The main aim of this research was to predict the stress concentration areas. The model was able to predict the part deformations due to thermal and residual stresses. 

_Polymers_ **2021** , _13_ , 3534 

15 of 20 



<!-- Start of picture text -->
s, 522<br>(Avg: 75%)<br>,150 MPa<br>85 MPa<br>-20 MPa<br>abe’<br><!-- End of picture text -->



<!-- Start of picture text -->
( a )<br>‘U, Magnitude<br>1.18mm<br>0.6mm<br>Omm<br>‘abe<br>( b )<br><!-- End of picture text -->

**Figure 8.** ( **a** ) Stresses in 3D printed polymer composite part after cooling down ( **b** ) warpage (exaggerated at a scale of 10). Reprinted with permission from reference [20]. Copyright 2018, Elsevier. 

## **4. Future Outlook** 

The fused filament fabrication process has been under continuous development since the commercial availability of this technology. Several studies reported experimental analysis and virtual modeling of different phases involved in the process. The numerical modeling of material flow inside/outside the printing head and behavior after deposition with promising outcomes have been reported. Based on the extensive literature review performed on numerical simulation techniques, the following research challenges and gaps are identified: 

- **Fiber Orientation:** The fiber orientation in deposited beads depends upon the material flow through the nozzle and deposition process. Most of the literature reports the use of Newtonian isotropic fluid properties; however, these materials should be modeled under anisotropic viscous flow conditions. Current modeling software cannot solve fourth or higher-order orientation tensors and cannot consider anisotropic flow characteristics (which is the case with fiber-reinforced composites). Therefore, there 

_Polymers_ **2021** , _13_ , 3534 

16 of 20 

is a need for better numerical simulation tools to consider realistic fiber orientation during material flow. 

- **Beads Deposition:** Several heat transfer models have been reported in the literature to predict the cooling process of the deposited beads. However, due to the anisotropy involved in the 3DP process, interlayer conduction phenomena need to be considered as thermal conductivities of deposited beads change with the fiber orientation. 

- **Interface and Bonding:** Bonding between the subsequent layers is highly correlated with the interface; therefore, the presence of fibers on the bead surface can affect this process. In addition, the necking phenomenon is derived by the gradients of surface tension is also influenced by the bead surface morphology. Finally, the material behavior (crystalline or amorphous) will reflect its viscosity, which ultimately affects the bonding process; therefore, it must be accounted for accurate process modeling. 

- _•_ **Integrated Simulation Models:** The FFF process is a complex multi-stage process as described in this paper. However, most reported computational work either focused on the material flow inside the liquefier or material behavior after deposition and is not as mature as the experimental literature. Therefore, there is a need for integrated studies considering all these phases of the FFF process (i.e., melt flow behavior inside/outside the nozzle, material deposition, solidification behavior, bond formation, and warpage and residual stresses). 

- **Model Validation:** The validation of numerical and analytical models is vital through experimental studies. Limited studies compared the numerical simulation results with experimental work, which is essential for validating and broader application of these models. 

- **Materials Portfolio:** Materials portfolio for the FFF process is rapidly growing. However, few materials (such as PLA and ABS) are considered for numerical and analytical modeling of process or material behavior. The researchers should focus on implementing existing models to a broader range of materials or develop models for materials not yet considered in the literature. 

- **Polymer Composites:** Two-phase materials (composites) are also barely considered for the numerical modeling of material or the FFF process. The most reported models address linear amorphous polymers. Different polymers exhibit different characteristics, such as bare PLA and ABS act as amorphous materials; however, PBT, PA12, and PEEK exhibit a semi-crystalline nature [84–86]. Moreover, the addition of the reinforcing phase can alter the nature of the resulting composite material, e.g., PLA acts as semi-crystalline material with tricalcium phosphate (TCP) [87]. The effect of reinforcement type and process parameters on polymer nature (amorphous or crystalline) will be worth addressing. 

## **5. Conclusions** 

This study provides a comprehensive review of state-of-the-art scientific achievements in numerical simulations for the FFF process of polymers and their composites. The first section presents an in-depth discussion on the physical phenomena involved in the FFF process and highlights the multi-level complexity. The subsequent section discusses the research efforts, specifically on numerical simulation techniques reported in the literature for the FFF process. 

The future of 3DP processes, specifically the FFF process, is promising due to research and development interest. However, several challenges are still faced. The focused research on the gaps mentioned above could further improve the process and material design. 

Currently, the FFF process is being explored extensively; however, the numerical simulation approaches are still empirically calibrated. This work has identified several issues persisting the wide use of numerical simulation techniques for its development. Addressing these research challenges will enable a more realistic and reliable prediction of the FFF process. 

_Polymers_ **2021** , _13_ , 3534 

17 of 20 

**Author Contributions:** Conceptualization, A.A.R. and M.K.; methodology, A.A.R.; software, A.A.R.; validation, A.A.R.; formal analysis, A.A.R.; investigation, A.A.R.; resources, M.K.; data curation, A.A.R.; writing—original draft preparation, A.A.R.; writing—review and editing, A.A.R. and M.K.; visualization, A.A.R.; supervision, M.K.; project administration, M.K.; funding acquisition, M.K. All authors have read and agreed to the published version of the manuscript. 

**Funding:** This research was partially funded by Qatar National Research Fund (QNRF) grant number NPRP13S-0126-200172, and APC was funded by College of Science and Engineering, Hamad Bin Khalifa University, Qatar Foundation, Doha, Qatar. 

**Institutional Review Board Statement:** Not applicable. 

### **Informed Consent Statement:** Not applicable. 

**Data Availability Statement:** Data sharing not applicable. 

**Conflicts of Interest:** The authors declare no conflict of interest. 

## **References** 

1. González-Henríquez, C.M.; Sarabia-Vallejos, M.A.; Rodriguez-Hernandez, J. Polymers for additive manufacturing and 4Dprinting: Materials, methodologies, and biomedical applications. _Prog. Polym. Sci._ **2019** , _94_ , 57–116. [CrossRef] 

2. Al Rashid, A.; Ahmed, W.; Khalid, M.Y.; Koç, M. Vat Photopolymerization of Polymer and Polymer Composites: Processes and Applications. _Addit. Manuf._ **2021** , _47_ , 102279. 

3. Al Rashid, A.; Khan, S.A.; Al-Ghamdi, S.G.; Koç, M. Additive manufacturing: Technology, applications, markets, and opportunities for the built environment. _Autom. Constr._ **2020** , _118_ , 103268. [CrossRef] 

4. Yilmaz, B.; Al Rashid, A.; Ait, Y.; Evis, Z.; Koç, M. Bioprinting: A review of processes, materials and applications. _Bioprinting_ **2021** , _23_ , e00148. [CrossRef] 

5. Ahangar, P.; Cooke, M.E.; Weber, M.H. Rosenzweig, D.H. Current biomedical applications of 3D printing and additive manufacturing. _Appl. Sci._ **2019** , _9_ , 1713. [CrossRef] 

6. Rane, K.; Strano, M. A comprehensive review of extrusion-based additive manufacturing processes for rapid production of metallic and ceramic parts. _Adv. Manuf._ **2019** , _7_ , 155–173. [CrossRef] 

7. Nachal, N.; Moses, J.A.; Karthik, P.; Anandharamakrishnan, C. Applications of 3D Printing in Food Processing. _Food Eng. Rev._ **2019** , _11_ , 123–141. [CrossRef] 

8. Ngo, T.D.; Kashani, A.; Imbalzano, G.; Nguyen, K.T.Q.; Hui, D. Additive manufacturing (3D printing): A review of materials, methods, applications and challenges. _Compos. Part B Eng._ **2018** , _143_ , 172–196. [CrossRef] 

9. Al Rashid, A.; Khan, S.A.; Al-Ghamdi, S.G.; Koç, M. Critical Review on 3DP Concrete trends, needs and research recommendations. In Proceedings of the International Conference of Materials and Engineering Technology (TICMET’20), Gaziantep, Turkey, 5–7 November 2020; p. 553. 

10. Crump, S.S. Apparatus and Method for Creating Three-Dimensional Objects. U.S. Patent 5,121,329A, 9 June 1992. 

11. Gibson, I.; Rosen, D.; Stucker, B. _Additive Manufacturing Technologies_ ; Springer: Berlin/Heidelber, Gemany, 2015. [CrossRef] 

12. Diegel, O.; Nordin, A.; Motte, D. Additive Manufacturing Technologies. In _A Practical Guide to Design for Additive Manufacturing_ ; Springer: Singapore, 2019; pp. 19–39. 

13. Al Rashid, A.; Khan, S.A.; Al-Ghamdi, S.G.; Koç, M. Additive Manufacturing of Polymer Nanocomposites: Needs and Challenges in Materials, Processes, and Applications. _J. Mater. Res. Technol._ **2021** , _14_ , 910–941. [CrossRef] 

14. Al Rashid, A.; Khalid, M.Y.; Imran, R.; Ali, U.; Koç, M. Utilization of Banana Fiber-Reinforced Hybrid Composites in the Sports Industry. _Materials_ **2020** , _13_ , 3167. [CrossRef] [PubMed] 

15. Shaqour, B.; Abuabiah, M.; Abdel-Fattah, S.; Juaidi, A.; Abdullah, R.; Abuzaina, W.; Qarout, M.; Verleije, B.; Cos, P. Gaining a better understanding of the extrusion process in fused filament fabrication 3D printing: A review. _Int. J. Adv. Manuf. Technol._ **2021** , _114_ , 1279–1291. [CrossRef] 

16. Bhandari, S.; Lopez-Anido, R.A.; Gardner, D.J. Enhancing the interlayer tensile strength of 3D printed short carbon fiber reinforced PETG and PLA composites via annealing. _Addit. Manuf._ **2019** , _30_ , 100922. [CrossRef] 

17. Nawafleh, N.; Celik, E. Additive manufacturing of short fiber reinforced thermoset composites with unprecedented mechanical performance. _Addit. Manuf._ **2020** , _33_ , 101109. [CrossRef] 

18. Al Rashid, A.; Koc, M. Creep and Recovery Behavior of Continuous Fiber-Reinforced 3DP Composites. _Polymers_ **2021** , _13_ , 1644. [CrossRef] [PubMed] 

19. Duty, C.; Ajinjeru, C.; Kishore, V.; Compton, B.; Hmeidat, N.; Chen, X.; Liu, P.; Hassen, A.A.; Lindahl, J.; Kunc, V. What makes a material printable? A viscoelastic model for extrusion-based 3D printing of polymers. _J. Manuf. Process._ **2018** , _35_ , 526–537. [CrossRef] 

20. Brenken, B.; Barocio, E.; Favaloro, A.; Kunc, V.; Pipes, R.B. Fused filament fabrication of fiber-reinforced polymers: A review. _Addit. Manuf._ **2018** , _21_ , 1–16. [CrossRef] 

_Polymers_ **2021** , _13_ , 3534 

18 of 20 

21. Seppala, J.E.; Migler, K.D. Infrared thermography of welding zones produced by polymer extrusion additive manufacturing. _Addit. Manuf._ **2016** , _12_ , 71–76. [CrossRef] 

22. Jiang, Z.; Diggle, B.; Tan, M.L.; Viktorova, J.; Bennett, C.W.; Connal, L.A. Extrusion 3D Printing of Polymeric Materials with Advanced Properties. _Adv. Sci._ **2020** , _7_ , 2001379. [CrossRef] 

23. Pocius, A.V.; Dillard, D.A. (Eds.) _Adhesion Science and Engineering: Surfaces, Chemistry and Applications_ ; Elsevier Science: Amsterdam, The Netherlands, 2002. 

24. Stansbury, J.W.; Idacavage, M.J. 3D printing with polymers: Challenges among expanding options and opportunities. _Dent. Mater._ **2016** , _32_ , 54–64. [CrossRef] [PubMed] 

25. McIlroy, C.; Graham, R.S. Modelling flow-enhanced crystallisation during fused filament fabrication of semi-crystalline polymer melts. _Addit. Manuf._ **2018** , _24_ , 323–340. [CrossRef] 

26. Shaqour, B.; Samaro, A.; Verleije, B.; Beyers, K.; Vervaet, C.; Cos, P. Production of drug delivery systems using fused filament fabrication: A systematic review. _Pharmaceutics_ **2020** , _12_ , 517. [CrossRef] [PubMed] 

27. Kim, J.Y.; Kim, S.Y.; Song, Y.S.; Youn, J.R. Relationship between the Crystallization Behavior and the Warpage of Film-InsertMolded Parts. _J. Appl. Polym. Sci._ **2010** , _116_ , 2658–2667. [CrossRef] 

28. Fitzharris, E.R.; Watanabe, N.; Rosen, D.W.; Shofner, M.L. Effects of material properties on warpage in fused deposition modeling parts. _Int. J. Adv. Manuf. Technol._ **2018** , _95_ , 2059–2070. [CrossRef] 

29. Ramanath, H.S.; Chua, C.K.; Leong, K.F.; Shah, K.D. Melt flow behaviour of poly-ε-caprolactone in fused deposition modelling. _J. Mater. Sci. Mater. Med._ **2008** , _19_ , 2541–2550. [CrossRef] 

30. Mostafa, N.; Syed, H.M.; Igor, S.; Andrew, G. A study of melt flow analysis of an ABS-Iron composite in fused deposition modelling process. _Tsinghua Sci. Technol._ **2009** , _14_ , 29–37. [CrossRef] 

31. Monzón, M.D.; Gibson, I.; Benítez, A.N.; Lorenzo, L.; Hernandez, P.M.; Marrero, M.D. Process and material behavior modeling for a new design of micro-additive fused deposition. _Int. J. Adv. Manuf. Technol._ **2013** , _67_ , 2717–2726. [CrossRef] 

32. Osswald, T.A.; Puentes, J.; Kattinger, J. Fused filament fabrication melting model. _Addit. Manuf._ **2018** , _22_ , 51–59. 

33. Wang, T.M.; Xi, J.T.; Jin, Y. A model research for prototype warp deformation in the FDM process. _Int. J. Adv. Manuf. Technol._ **2007** , _33_ , 1087–1096. [CrossRef] 

34. Armillotta, A.; Bellotti, M.; Cavallaro, M. Warpage of FDM parts: Experimental tests and analytic model. _Robot. Comput. Integr. Manuf._ **2018** , _50_ , 140–152. [CrossRef] 

35. Folgar, F.; Tucker, C.L. Orientation Behavior of Fibers in Concentrated Suspensions. _J. Reinf. Plast. Compos._ **1984** , _3_ , 98–119. [CrossRef] 

36. Advani, S.G.; Tucker, C.L. The Use of Tensors to Describe and Predict Fiber Orientation in Short Fiber Composites. _J. Rheol._ **1987** , _31_ , 751–784. [CrossRef] 

37. Nixon, J.; Dryer, B.; Lempert, I.; Bigio, D.I. Three parameter analysis of fiber orientation in fused deposition modeling geometries. In Proceedings of the 30th International Conference of the Polymer Processing Society, Cleveland, OH, USA, 6–12 June 2014. 

38. Garcia, A. Nozzle Geometry Effects on Exit Orientation of Short Fiber Composites. Master’s Thesis, Wichita State University, Wichita, KS, USA, May 2017. 

39. Heller, B.P.; Smith, D.E.; Jack, D.A. Effects of extrudate swell and nozzle geometry on fiber orientation in Fused Filament Fabrication nozzle flow. _Addit. Manuf._ **2016** , _12_ , 252–264. [CrossRef] 

40. Yang, D.; Wu, K.; Wan, L.; Sheng, Y. A Particle Element Approach for Modelling the 3D Printing Process of Fibre Reinforced Polymer Composites. _J. Manuf. Mater. Process._ **2017** , _1_ , 10. 

41. Brenken, B.; Favaloro, A.; Barocio, E.; DeNardo, N.M.; Pipes, R.B. Development of a model to predict temperature history and crystallization behavior of 3dprinted parts made from fiber-reinforced thermoplastic polymers. In Proceedings of the SAMPE Conference 2016, Long Beach, CA, USA, 23–26 May 2016. 

42. Zhou, Y.; Nyberg, T.; Xiong, G.; Liu, D. Temperature Analysis in the Fused Deposition Modeling Process. In Proceedings of the 2016 3rd International Conference on Information Science and Control Engineering (ICISCE), Beijing, China, 8–10 July 2016; pp. 678–682. 

43. Danoglidis, P.A.; Falara, M.G.; Katotriotou, M.K.; Konsta-Gdoutos, M.S.; Gdoutos, E.E. Mechanics of Composite and Multifunctional Materials. In Proceedings of the SEM Annual Conference and Exposition on Experimental and Applied Mechanics, Costa Mesa, CA, USA, 8–11 June 2015. 

44. Bellehumeur, C.; Li, L.; Sun, Q.; Gu, P. Modeling of bond formation between polymer filaments in the fused deposition modeling process. _J. Manuf. Process._ **2004** , _6_ , 170–178. [CrossRef] 

45. Stewart, S.R.; Wentz, J.E.; Allison, J.T. Experimental and Computational Fluid Dynamic Analysis of Melt Flow Behavior in Fused Deposition Modelling of Poly(lactic) Acid. In Proceedings of the ASME 2015 International Mechanical Engineering Congress and Exposition, Houston, TX, USA, 13–19 November 2015. [CrossRef] 

46. Papon, M.E.A.; Haque, A.; Sharif, M.A.R. Effect of nozzle geometry on Melt flow simulation and structural property of thermoplastic nanocomposites in Fused deposition modeling. In Proceedings of the 32nd Technical Conference of the American Society for Composites 2017, West Lafayette, IN, USA, 23–25 October 2017; pp. 2167–2182. 

47. Xinhua, L.; Shengpeng, L.; Zhou, L.; Xianhua, Z.; Xiaohu, C.; Zhongbin, W. An investigation on distortion of PLA thin-plate part in the FDM process. _Int. J. Adv. Manuf. Technol._ **2015** , _79_ , 1117–1126. [CrossRef] 

_Polymers_ **2021** , _13_ , 3534 

19 of 20 

48. Wijnen, B.; Sanders, P.; Pearce, J.M. Improved model and experimental validation of deformation in fused filament fabrication of polylactic acid. _Prog. Addit. Manuf._ **2018** , _3_ , 193–203. [CrossRef] 

49. Xia, H.; Lu, J.; Tryggvason, G. A numerical study of the effect of viscoelastic stresses in fused filament fabrication. _Comput. Methods Appl. Mech. Eng._ **2019** , _346_ , 242–259. [CrossRef] 

50. Ortega, Z.; Alemán, M.E.; Benítez, A.N.; Monzon, M.D. Theoretical-experimental evaluation of different biomaterials for parts obtaining by fused deposition modeling. _Meas. J. Int. Meas. Confed._ **2016** , _89_ , 137–144. [CrossRef] 

51. Watanabe, N. Computational and Experimental Investigation of Reinforced Polymers for Material Extrusion Additive Manufacturing. Master’s Thesis, Georgia Institute of Technology, Atlanta, GA, USA, December 2016. 

52. Kim, T.; Trangkanukulkij, R.; Kim, W.S. Nozzle Shape Guided Filler Orientation in 3D Printed Photo-curable Nanocomposites. _Sci. Rep._ **2018** , _8_ , 3805. [CrossRef] 

53. Lewicki, J.P.; Rodriguez, J.N.; Zhu, C.; Worsley, M.A.; Wu, A.S.; Kanarska, Y.; Horn, J.D.; Duoss, E.B.; Ortega, J.M.; Elmer, W.; et al. 3D-Printing of Meso-structurally Ordered Carbon Fiber/Polymer Composites with Unprecedented Orthotropic Physical Properties. _Sci. Rep._ **2017** , _7_ , 43401. [CrossRef] 

54. Bellini, A. Fused Deposition of Ceramics: A Comprehensive Experimental, Analytical and Computational Study of Material Behavior, Fabrication Process and Equipment Design. Ph.D. Thesis, Drexel University Philadelphia, Philadelphia, PA, USA, September 2002. 

55. Mellor, L.F.; Huebner, P.; Cai, S.; Mohiti-Asli, M.; Taylor, M.A.; Spang, J.; Shirwaiker, R.A.; Loboa, E.G. Fabrication and Evaluation of Electrospun, 3D-Bioplotted, and Combination of Electrospun/3D-Bioplotted Scaffolds for Tissue Engineering Applications. _Biomed. Res. Int._ **2017** , _2017_ , 6956794. [CrossRef] [PubMed] 

56. Palmero, E.M.; Casaleiz, D.; de Vicente, J.; Hernández-Vicen, J.; López-Vidal, S.; Ramiro, E.; Bollero, A. Composites based on metallic particles and tuned filling factor for 3D-printing by Fused Deposition Modeling. _Compos. Part A Appl. Sci. Manuf._ **2019** , _124_ , 105497. [CrossRef] 

57. Kulich, D.M.; Gaggar, S.K.; Lowry, V.; Stepien, R. Acrylonitrile–Butadiene–Styrene (ABS) Polymers. In _Kirk-Othmer Encyclopedia of Chemical Technology_ ; John Wiley & Sons: Hoboken, NJ, USA, 2003. [CrossRef] 

58. Cress, A.K.; Huynh, J.; Anderson, E.H.; O’neill, R.; Keles, O. Effect of recycling on the mechanical behavior and structure of additively manufactured acrylonitrile butadiene styrene (ABS). _J. Clean. Prod._ **2021** , _279_ , 123689. [CrossRef] 

59. Bellini, A.; Guceri, S.; Bertoldi, M. Liquefier Dynamics in Fused Deposition. _J. Manuf. Sci. Eng._ **2004** , _126_ , 237–246. [CrossRef] 60. Carrasco, F.; Pagès, P.; Gámez-Pérez, J.; Santana, O.O.; Maspoch, M.L. Processing of poly(lactic acid): Characterization of chemical structure, thermal stability and mechanical properties. _Polym. Degrad. Stab._ **2010** , _95_ , 116–125. [CrossRef] 

61. Zhang, Q.; Lei, H.; Cai, H.; Han, X.; Lin, X.; Qian, M.; Zhao, Y.; Huo, E.; Villota, E.M.; Mateo, W. Improvement on the properties of microcrystalline cellulose/polylactic acid composites by using activated biochar. _J. Clean. Prod._ **2020** , _252_ , 119898. [CrossRef] 

62. Tian, X.; Liu, T.; Wang, Q.; Dilmurat, A.; Li, D.; Ziegmann, G. Recycling and remanufacturing of 3D printed continuous carbon fiber reinforced PLA composites. _J. Clean. Prod._ **2017** , _142_ , 1609–1618. [CrossRef] 

63. Yunus, D.E.; Shi, W.; Sohrabi, S.; Liu, Y. Shear induced alignment of short nanofibers in 3D printed polymer composites. _Nanotechnology_ **2016** , _27_ , 495302. [CrossRef] 

64. Yunus, D.E.; He, R.; Shi, W.; Kaya, O.; Liu, Y. Short fiber reinforced 3d printed ceramic composite with shear induced alignment. _Ceram. Int._ **2017** , _43_ , 11766–11772. [CrossRef] 

65. Mulholland, T.; Goris, S.; Boxleitner, J.; Osswald, T.A.; Rudolph, N. Process-Induced Fiber Orientation in Fused Filament Fabrication. _J. Compos. Sci._ **2018** , _2_ , 45. [CrossRef] 

66. Russell, T.; Heller, B.; Jack, D.A.; Smith, D.E. Prediction of the Fiber Orientation State and the Resulting Structural and Thermal Properties of Fiber Reinforced Additive Manufactured Composites Fabricated Using the Big Area Additive Manufacturing Process. _J. Compos. Sci._ **2018** , _2_ , 26. [CrossRef] 

67. Bertevas, E.; Férec, J.; Khoo, B.C.; Ausias, G.; Phan-Thien, N. Smoothed particle hydrodynamics (SPH) modeling of fiber orientation in a 3D printing process. _Phys. Fluids_ **2018** , _30_ , 103103. [CrossRef] 

68. Shahriar, B.B.; France, C.; Valerie, N.; Arthur, C.; Christian, G. Toward improvement of the properties of parts manufactured by FFF (fused filament fabrication) through understanding the influence of temperature and rheological behaviour on the coalescence phenomenon. _AIP Conf. Proc._ **2017** , _1896_ , 040008. 

69. Yardimci, M.A.; Hattori, T.; Guceri, S.I.; Danforth, S.C. Thermal analysis of Fused Deposition. In Proceedings of the 1997 International Solid Freeform Fabrication Symposium, Austin, TX, USA, 11–13 August 1997; pp. 689–698. 

70. Liu, J.; Anderson, K.L.; Sridhar, N. Direct Simulation of Polymer Fused Deposition Modeling (FDM)—An Implementation of the Multi-Phase Viscoelastic Solver in OpenFOAM. _Int. J. Comput. Methods_ **2020** , _17_ , 1844002. [CrossRef] 

71. Sun, Q. Bond Formation between Polymer Filaments in Fused Deposition Modeling Process. Master’s Thesis, University of Calgary, Calgary, AB, Canada, August 2005. [CrossRef] 

72. Sun, Q.; Rizvi, G.M.; Bellehumeur, C.T.; Gu, P. Effect of processing conditions on the bonding quality of FDM polymer filaments. _Rapid. Prototyp. J._ **2008** , _14_ , 72–80. [CrossRef] 

73. Gurrala, P.K.; Regalla, S.P. Part strength evolution with bonding between filaments in fused deposition modelling. _Virtual Phys. Prototyp._ **2014** , _9_ , 141–149. [CrossRef] 

74. Costa, S.F.; Duarte, F.M.; Covas, J.A. Towards modelling of Free Form Extrusion: Analytical solution of transient heat transfer. _Int. J. Mater. Form._ **2008** , _1_ , 703–706. [CrossRef] 

_Polymers_ **2021** , _13_ , 3534 

20 of 20 

75. Costa, S.F.; Duarte, F.M.; Covas, J.A. Estimation of filament temperature and adhesion development in fused deposition techniques. _J. Mater. Process. Technol._ **2017** , _245_ , 167–179. [CrossRef] 

76. McIlroy, C.; Olmsted, P.D. Disentanglement effects on welding behaviour of polymer melts during the fused-filament-fabrication method for additive manufacturing. _Polymer_ **2017** , _123_ , 376–391. [CrossRef] 

77. McIlroy, C.; Olmsted, P.D. Deformation of an amorphous polymer during the fused-filament-fabrication method for additive manufacturing. _J. Rheol._ **2017** , _61_ , 379–397. [CrossRef] 

78. Zhang, Y.; Chou, K. A parametric study of part distortions in fused deposition modelling using three-dimensional finite element analysis. _Proc. Inst. Mech. Eng. Part B J. Eng. Manuf._ **2008** , _222_ , 959–968. [CrossRef] 

79. Xia, H.; Lu, J.; Tryggvason, G. Fully resolved numerical simulations of fused deposition modeling. Part II–solidification, residual stresses and modeling of the nozzle. _Rapid Prototyp. J._ **2018** , _24_ , 973–987. [CrossRef] 

80. Xia, H.; Lu, J.; Tryggvason, G. Simulations of fused filament fabrication using a front tracking method. _Int. J. Heat. Mass. Transf._ **2019** , _138_ , 1310–1319. [CrossRef] 

81. Cattenone, A.; Morganti, S.; Alaimo, G.; Auricchio, F. Finite Element Analysis of Additive Manufacturing Based on Fused Deposition Modeling: Distortions Prediction and Comparison with Experimental Data. _J. Manuf. Sci. Eng._ **2019** , _141_ , 011010. [CrossRef] 

82. Favaloro, A.J.; Barocio, E.; Brenken, B.; Pipes, R.B. Simulation of Polymeric Composites Additive Manufacturing using Abaqus. In Proceedings of the Dassault Systemes’ Science in the Age of Experience, Chicago, IL, USA, 15–18 May 2017; pp. 103–114. 

83. Talagani, M.R.; Dormohammadi, S.; Dutton, R.; Godines, C.; Baid, H.; Abdi, F.; Kunc, V.; Compton, B.; Simunovic, S.; Duty, C. Numerical Simulation of Big Area Additive Manufacturing (3D Printing) of a Full Size Car. _SAMPE J._ **2015** , _51_ , 27–36. 

84. Gnanasekaran, K.; Heijmans, T.; van Bennekom, S.; Woldhuis, H.; Wijnia, S.; de With, G.; Friedrich, H. 3D printing of CNT-and graphene-based conductive polymer nanocomposites by fused deposition modeling. _Appl. Mater. Today_ **2017** , _9_ , 21–28. [CrossRef] 

85. Li, H.; Zhang, S.; Yi, Z.; Li, J.; Sun, A.; Guo, J.; Xu, G. Bonding quality and fracture analysis of polyamide 12 parts fabricated by fused deposition modeling. _Rapid Prototyp. J._ **2017** , _23_ , 973–982. [CrossRef] 

86. Wu, W.; Geng, P.; Li, G.; Zhao, D.; Zhang, H.; Zhao, J. Influence of Layer Thickness and Raster Angle on the Mechanical Properties of 3D-Printed PEEK and a Comparative Mechanical Study between PEEK and ABS. _Materials_ **2015** , _8_ , 5834–5846. [CrossRef] 

87. Drummer, D.; Cifuentes-Cuéllar, S.; Rietzel, D. Suitability of PLA/TCP for fused deposition modeling. _Rapid Prototyp. J._ **2012** , _18_ , 500–507. [CrossRef] 

