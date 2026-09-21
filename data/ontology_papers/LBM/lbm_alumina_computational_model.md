International Journal of Machine Tools & Manufacture 48 (2008) 1345– 1353 



Contents lists available at ScienceDirect 

# International Journal of Machine Tools & Manufacture 

journal homepage: www.elsevier.com/locate/ijmactool 



# Computational predictions in single-dimensional laser machining of alumina Anoop N. Samant, Narendra B. Dahotre<sup>�</sup> 

Department of Materials Science and Engineering, The University of Tennessee, Knoxville, TN 37996, USA 

a r t i c l e i n f o a b s t r a c t Article history: Machining of alumina was investigated in this study by using a JK 701 pulsed Nd:YAG laser. A Received 25 January 2008 hydrodynamic machining model was developed which incorporated the effect of multiple reflections on Received in revised form the amount of laser energy absorbed, the thermal effects for melting the material, vapor pressure effect 15 May 2008 for expelling out the molten material, material losses due to evaporation and the inverse effect of Accepted 25 May 2008 surface tension on the expelled depth .The model also incorporated the transient effect of laser beam Available online 7 <u>July</u> 2008 de-focusing due to change in machined depth as a function of expelled material during machining for Keywords: precise estimation of the melted depth during each pulse. It was observed that the material removal was Machining a combination of melt expulsion and evaporation processes. The developed model would be an excellent Alumina tool for advance prediction of the total thermal energy and time required for removal and/or machining Pulsed mode laser of desired depth of material. Recoil pressure & 2008 Elsevier Ltd. All rights reserved. 

## 1. Introduction 

Outstanding mechanical and physical properties like high hardness, chemical stability and high thermal resistance have encouraged the use of engineering ceramics such as alumina, silicon nitride, zirconia and silicon carbide in several applications. These ceramics are widely used for making machine tools, valves, rotors, optical and electronic devices [1–5] and in medical applications for components such as artificial joints [6,7]. 

High hardness and brittleness make the ceramics difficult to machine using conventional techniques that are mostly based on mechanical grinding and fracturing (cutting). The damage caused on the surface by the machining of ceramics employing these techniques can affect the strength and efficiency of the components thereby creating a hurdle in their widespread utilization in above-mentioned applications. Hence, a vital step in the manufacturing of ceramic components is their cost-effective machining with excellent quality. Extensive research on precision machining of ceramic components has been conducted over the past several years, developing numerous advanced technologies in grinding, cutting and polishing. Out of all the techniques for ceramic machining, grinding is still considered to be the most desirable and reliable [8]. Although conventional grinding fulfills the necessities for dimensional accuracy and surface finish, prohibitively longer times to machine them and high machining costs amounting to 60–90% of the final cost of the end product pose a major drawback for the grinding process [9,10]. Furthermore, 

> � Corresponding author. Tel.: +1865 974 3609; fax: +1865 974 4115. 

> E-mail address: ndahotre@utk.edu (N.B. Dahotre). 

ground products often demonstrate surface and subsurface cracks [11–13], some amount of plastic deformation [14], pulverization layers [15,16] and significant surface residual stresses [17]. Hence, there is a requirement for ceramic processing techniques which can reduce tool wear, enhance the material removal rates and improve the surface finish of the components. 

Ultrasonic machining removes materials by the impact motion of ultrasonically vibrated abrasive particles. However, the mechanism of material removal is not very well documented, thus making the process optimization difficult [18]. Recent developments in the field of electrical discharge machining (EDM) have permitted the use of this technology for manufacturing conductive ceramic materials [19]. Electro-chemical discharge machining (ECDM) which has combined features of EDM and electrochemical machining (ECM) is capable of machining high strength electrically non-conductive materials. However, as a significant portion of the total heat developed is dissipated for increasing the temperature of the electrolyte, the material removed while machining is less, thus making the process incompetent [20]. 

Over the past few years, laser machining (LM) has been considered as a potential technique for acquiring high material removal rates in machining ceramic materials [6]. Laser machining is an operation similar to laser drilling subsequently conducted on neighboring locations. Both the processes involve material removal via melting or decomposition, and vaporization and physical expulsion of these phases from the region of laser–material interaction. Thus the physical phenomena governing both machining and drilling are similar. The temporally and spatially intense and restricted heat source of laser power provides an extremely efficient method to increase the 

0890-6955/$ - see front matter & 2008 Elsevier Ltd. All rights reserved. doi:10.1016/j.ijmachtools.2008.05.004 

A.N. Samant, N.B. Dahotre / International Journal of Machine Tools & Manufacture 48 (2008) 1345–1353 

1346 

temperature of the work piece making the machining process convenient. 

Escalating interest in the use of lasers for manufacturing can be attributed to the several benefits such as non-contact processing, capability of automation, reduced manufacturing costs, efficient material utilization, reduced heat-affected zone (HAZ), high productivity and eradication of finishing operations [21,22]. Laser machining of ceramics is widely used in the aerospace industry for generating closely spaced holes in turbine engine components and also in the micro-electronics industry for drilling holes with high aspect ratios at designated locations [23]. Pulsed lasers can be successfully used to carry out micro-drilling on zirconia and the process parameters can be controlled to drill holes in the zirconia ceramic [21] which can be used in bearings, oxygen sensors, fuel cells and pH meters [24]. The hole diameter at the entry is more than the diameter at the exit leading to a positive taper to several of the drilled holes. However, this effect can be minimized by using a lens of long focal length with longer focal waist. As laser drilling has tremendous applications, understanding the drilling mechanism is extremely vital in order to efficiently control the processing parameters and thus the associated surface features. 

Alumina is widely used as a substrate in hybrid circuits as it possesses high dielectric strength and thermal stability [25,26]. Due to its high hardness, strength and corrosion resistance at high temperature, machining of alumina is carried out for different applications. During laser machining, the phenomena occurring in the area of interaction between the laser beam and the ceramic such as but not limited to material removal, ablation, melting, evaporation, absorption of energy by the solid, and reflection of energy from the surface depend on the processing parameters (energy, repetition rate, pulse duration and peak power of the laser) and on the chemical and physical properties of the material. Hence, the present study aims at understanding the physical phenomena underlying the machining of alumina ceramic by pulsed Nd:YAG laser and develops a computational approach to predict the effect of the laser processing parameters on the depth of the machined region. In this approach, single-dimensional laser machining of ceramics for applications such as drilling has been 

demonstrated. Multidimensional laser machining of ceramics by the linear or non-linear movement of the laser beam for applications such as cutting will be discussed in future work. 

## 2. Laser processing 

Dense alumina ceramic obtained from a commercial source (Coorstek, Golden, CO) in the form of disc of 89 mm diameter and 4 mm thickness was used for the machining purpose. The alumina surface was exposed to a JK 701 pulsed Nd:YAG laser (1064 nm wavelength) from GSI Lumonics, Rugby, England. The laser offered pulse energies from 0.1 to 55 J, repetition rates from 0.2 to 500 Hz, and the pulse width from 0.3 to 20 ms. By varying the repetition rate, peak power and pulse width in different combinations, a set of parameters were recognized that generated adequate interaction between the laser beam and the ceramic surface for required machining of alumina disc. For a pulse energy of 4 J, repetition rate of 20 Hz and a pulse width of 0.5 ms, reasonable interaction was observed between the laser and the ceramic surface that was capable of machining a cavity. Hence for this set of parameters, several pulses (5, 10, 20 and 30) were applied on the ceramic surface and the corresponding depth in the cross-section of machined cavity was measured from the optical micrograph (Fig. 1). The figure also includes the top views of machined cavities on the top surface of the alumina disc. The given number of pulses were chosen to machine blind cavities of various depths and also a cavity through the entire thickness of plate. The number of pulses were applied to the ceramic randomly and not in any systematic order in order to avoid the influence of lurking variables such as change of surrounding temperature, relative humidity and so on that could affect the drill depth to some extent. Thus the standard procedure of randomizing the experimental runs was implemented in this study. It was observed that under the present set of laser parameters (4 J, 20 Hz, 0.5 ms) application of 30 pulses machined through the entire thickness of the alumina disc (4 mm). However, foresighting the exact number of pulses required to machine a certain cavity depth is an exigent task. Hence, developing a mathematical model 



<!-- Start of picture text -->
0.26 mm $ Satter5 osémm| & a After 10<br>pulses bs S: pulses<br>Pee” CROSS SECTION 500 jim cross secTion<br>P| atter30 ‘eal<br>f\ pulses S. 3.23pulses mm<br>4.0mm<br>| 500 a 500 pm 500 ym<br>CROSS SECTION ) We - CROSS SECTION<br><!-- End of picture text -->

Fig. 1. Cross-sectional and top views of the cavities machined in alumina disc with different number of pulses. 

A.N. Samant, N.B. Dahotre / International Journal of Machine Tools & Manufacture 48 (2008) 1345–1353 

1347 

based on the processing data for such predictions is the most suitable approach. 

## 3. Computational predictions 

Laser machining is accomplished when the work piece absorbs laser energy and this photon energy gets converted into thermal energy. The magnitude of the laser energy absorbed depends on the initial absorptivity of the material and the amount of multiple reflections within the machined cavity. The temperature at the surface of the ceramic changes because of this absorbed energy. When the temperature rises beyond the melting point or the decomposition temperature, the phase of the material changes and it melts and/or evaporates [27]. The high peak intensity of the pulse generates strong evaporation pressure which is responsible for ejection of this molten material and material loss at the surface due to evaporation for generation of machined depth. However, the surface tension of molten material reduces the depth of penetration to some extent [28]. Although, in the past majority of works have considered material removal only through direct evaporation [29–32] in the present work the material removal will be based on a mixed phenomenon comprising of both the melt expulsion and evaporation. The above-mentioned effects will be systematically considered in the present study. A complete model of material removal (machining) by laser beam interaction with the ceramic surface could consider many more phenomena than those considered here. Complexities generated by other physical processes during laser–material interactions will be demonstrated in subsequent publications. As the physical processes occurring along the depth are entirely different from those occurring at the surface, this study aims at predicting only the depth rather than estimating the width (diameter of a machined cavity) of material removed/machined at the surface. Efforts are on going to predict the width of material machined (diameter) and will be incorporated in due course of time. 

## 3.1. Temporal evolution 

To estimate the depth of machined region for a given set of laser processing parameters considering the above mentioned 

effects, the temperature at the surface and the corresponding thermal gradient within the material were predicted. The heating during pulse on and the subsequent cooling during pulse off over the entire time of machining operation were considered for determining the heating curve by taking into account the ON and OFF times during machining under present set of laser parameters. The schematic illustrating the pulse ON–OFF is shown in Fig. 2 while the process parameters and the corresponding machined depths measured optically are represented in Table 1. 

There is a temperature drop when the laser is switched off after the first pulse which is followed by a temperature rise when the laser is switched on again for the next pulse. The simulations were run till the operation time was completed for each case. A detailed procedure explaining the predictions of depth of material removed (machined) from the alumina disc will be explained in the later sections. The computations were started with estimation of the maximum temperature reached after the first pulse by using a three-dimensional heat transfer flow model developed in COMSOL’s heat transfer mode [33] using Fourier’s second law of heat transfer: 



where T is the temperature field, t is the time and x, y and z are the spatial directions. The term a(T) is the temperaturedependent thermal diffusivity of the material which is given by k(T)/rCp(T), where r is the density (3.8 g/cm<sup>3</sup> ) [34], Cp(T) is the temperature-dependent specific heat of the material (J/kg K) and k(T) is the temperature-dependent thermal conductivity of the material (W/m K) [35]. At time t ¼ 0, the initial temperature of T ¼ T0 ¼ 300 K was applied. The equilibrium between the laser energy absorbed at the surface and the losses due to radiation is given by 







Fig. 2. Schematic of pulse ON–OFF. 

Table 1 

Parameters of laser processing 

|Number of|Operation|Pulse width (ON|OFF time|Total ON|Total OFF|Cavity depth|
|---|---|---|---|---|---|---|
|pulses|time (s)|time) (ms)|(ms)|time (ms)|time (ms)|(mm)|
|5|0.25|0.5|49.5|2.5|247.5|0.26|
|10|0.5|0.5|49.5|5.0|495.0|0.56|
|20|1.0|0.5|49.5|10.0|990.0|3.23|
|30|1.5|0.5|49.5|15.0|1485.0|4.0|



A.N. Samant, N.B. Dahotre / International Journal of Machine Tools & Manufacture 48 (2008) 1345–1353 

1348 

where k is the thermal conductivity of the material (W/m K), e is emissivity for thermal radiation (0.7) [35], a is the absorptivity of the material (0.8) [34], I is laser power intensity, tp is the operation time and s is the Stefan–Boltzmann constant (5.67 � x 10<sup>�</sup> 7<sup>8</sup> W/m<sup>2</sup> K<sup>4</sup> ). Laser-induced machining is a rapid heating and cooling process due to which the thermophysical properties of materials exposed to the laser beam change rapidly in a large temperature range. Changes in thermal conductivity and specific heat as a function of temperature [35] (Fig. 3) were incorporated to provide better accuracy in calculations. The latent heat of fusion was taken into account by including the variation of specific heat as a function of temperature. 

Multiple reflections of the laser beam are extremely important for high aspect ratio drill cavities (Fig. 1) and they govern the flow of energy from the laser to the surface of the material being machined [36]. This phenomenon has been incorporated into the machining process in different ways [37–41]. Bang and Modest [42] found that the effective absorptivity of the material is increased due to the phenomena of multiple reflections and in process such as high aspect ratio laser drilling it is expected to instantaneously reach the value of 100% [43,44]. Nonetheless, accurate in-situ absorptivity measurements being difficult for rapid process like laser processing, in this study, for comparison purpose the computations were conducted by considering three different values of absorptivity that included the literature value of 0.8 mentioned above [34], 0.9 and 1 (corresponding to an absorption of 100%). The resultant effect of these absorptivity values on the machined depth is discussed later. Although it is very difficult in an extremely short duration high-energy density dynamic process like laser–material interaction to accurately conduct in-situ absorptivity measurements, attempts are going on in parallel to measure the actual absorptivity values under the laser processing conditions similar to the ones employed in the present work and they will be incorporated in the future calculations. The convection occurring at the bottom surface of the disc is given by 



where L is the thickness of the disc (4 mm) and h(T) is the heat transfer coefficient (W/m<sup>2</sup> K) considered as a function of temperature. It was assumed that no heat loss took place through the other surfaces. The variation of heat transfer coefficient was also included as a function of temperature [45]. After solving this model, the maximum surface temperature reached after the first pulse was determined which was input in Eq. (4) below to predict 

the temperature reached after the laser is switched off [27]: 



where Ti is the temperature during heating of pulse i (K), T0 is the ambient temperature of 300 K, toff is the OFF period between successive pulses and erf ( ) is the error function. When the laser is active, the surface temperature is given by [27] **f f f f f f f f f f** 



where T<sup>0</sup> i�1<sup>isthetemperatureduringcoolingoftheearlierpulse</sup> (K) predicted from Eq. (4) above, W is the incident beam power, ton is the pulse duration and r is the beam radius (0.12 mm). The temperatures reached during the ON and OFF periods of the successive pulses were determined by repeatedly solving Eqs. (4) and (5) till the operation time was reached. 

As this study does not focus on the microstructure evolution after the pulsing was stopped, the cooling curves have not been discussed. By tracking the depth at which the melting point or decomposition temperature of alumina (2323 K [46]) was reached, the melt depth (zt) from the surface at any instant was estimated from the heating curves and further depth calculations were based on this depth. Alumina is stable up to the melting point after which it melts and forms the liquid which is stable till about 3500 K. Due to the dissociation of alumina at temperatures above 3250 K, sub-oxides of aluminum, aluminum metal vapor and oxygen gas are formed. The majority of the stable species formed above 3250 K comprises of AlO(g) and Al(g) while minor amounts of Al2O(g) and AlO2(g) are formed. At temperatures above 5000 K, the sub-oxides dissociate completely forming aluminum vapor and atomic oxygen [47]. Laser machining takes place due to the expulsion of the liquid phase formed during the dissociation process as can be seen from the presence of several droplets or humps of solidified material around the drilled hole. (Fig. 1) 



where mv is mass of vapor molecule (molecular weight of alumina/ Avogadro’s number ¼ 1.693 � —_ 10<sup>�25</sup> kg/at), k is the Boltzmann constant (1.38065 � — 10<sup>�23</sup> J/K), Ts is the surface temperature and p(Ts) is the saturation pressure given by Clausius–Clapeyron equation: Lv=kT e pðT sÞ ¼ p0 exp (7) <u>�1 �</u> T e=Ts� 

where p0 is the ambient pressure (1.013 � x 10<sup>5</sup> N/m<sup>2</sup> ), Lv is latent heat of evaporation (1066.5 J/g) [34] and Te is the vaporization temperature (3253 K [48]). The corresponding depth of material evaporated at a given instant was predicted from the rate of evaporation by the relation: 



The cumulative evaporated depths (for 100% absorption) at different time instants is represented in Fig. 4. The evaporated depth (zeva) was subtracted from the melt depth (zt) to give the available melt pool (zava). The corresponding drop in temperature at any instant at the surface because of the cooling of the melt pool by evaporation was given by [49] **f f f f f f f f f f f f f f f f f f f f f f f f f f f f** 



Fig. 3. Variation in specific heat and thermal conductivity with temperature [35]. 

A.N. Samant, N.B. Dahotre / International Journal of Machine Tools & Manufacture 48 (2008) 1345–1353 

1349 



<!-- Start of picture text -->
5. After 5 pulses 3 After 10 pulses<br>sé BE 3<br>E= g2<br>4 mp ss 2<br>333 sé,<br>— €<br>55<br>o0°0<br>)0.4 0.2 0.3 o 0.2 0.4 06<br>Time (sec) Time (sec)<br>3 2 zy 2<br>3 After 30 pulses s After 20 pulses<br>ie”s tgss<br>gs~ 10 = B=€<br>£3 £3<br>Bo , Bo 4<br>FIEE3<br>Oo50 cs)5 0<br>0 05 1 15 0 025 05 0.75 1<br>Time (sec) Time (sec)<br><!-- End of picture text -->

Fig. 4. Cumulative evaporated depth (for 100% absorption). 



<!-- Start of picture text -->
xx<br>=<br>x 04 2x<br>< E04<br>¢g<br>Z02 = 2<br>5 g 0.2<br>5 z<br>roo 0<br>0 01 02 03 0 0.2 04<br>Time (sec) Time (sec)<br>> 08 08<br>Sos = 06<br>Sos ome bs<br>==<br>202 B oa<br>£<br>£ 5<br>oo<br>00s 1 15 ° 0.25 Os 0.75 1<br>Time (sec) Time (sec)<br><!-- End of picture text -->

Fig. 5. Heating curves for different number of pulses (for 100% absorption). 

This drop in temperature was subtracted from the temperature predicted by Eqs. (4) and (5) above to give the actual surface temperature (for 100% absorption) at any given time instant as represented in Fig. 5 which has a winding nature because the temperature drops during the OFF time and rises during the ON time of the laser. As the evaporation losses represented in Fig. 4 were a function of the surface temperature, the increase in the cumulative evaporated depth was more (steeper slope) during the ON time due to rise in temperature compared to the increase in the cumulative evaporated depth during the OFF time when the temperature drop leads to a gentle slope during the OFF time. The 

losses due to evaporation begin to take place after the surface temperature exceeds the vaporization temperature of alumina (3253 K [48]) after a certain number of pulses. 

## 3.2. Recoil pressure and surface tension effects 

In laser machining, material removal takes place primarily in the liquid and vapor phases. The expulsion of the molten material is driven by the recoil pressure stimulated due to the evaporation of the melt surface exposed to the laser beam [50]. The recoil 

A.N. Samant, N.B. Dahotre / International Journal of Machine Tools & Manufacture 48 (2008) 1345–1353 

1350 

pressure stimulates ejection of the melt flow from the interaction zone at very high velocities [51]. The effective melt depth (zeff) will be available for expulsion for the next time instant and it would be the portion remaining after a fraction of the available melt depth (zava) was expelled by the recoil pressure pe given by [52] 



where Lv is latent heat of evaporation (1066.5 J/g) [34], and m<sup>2</sup> ¼ kTs=mvLv, where mv is mass of the vapor molecule (1.693 � — 10<sup>�25</sup> kg/at) [34] and Ts is the surface temperature. Predictions of this fraction of the melt pool that is expelled by the recoil pressure will follow later in this section. In the absence of this recoil pressure, the thin film of molten material formed around the machined cavity would be responsible for closing the cavity. Thus the temperature field predicted in Section 3.1 above assisted in determining the evaporation-provoked recoil pressure at the surface during laser machining of alumina ceramic using 

the experimentally verified physical model of melt hydrodynamics proposed by Anisimov [52] (Eq. (10)). 

It has been observed in the past that besides the recoil pressure, the surface tension also affects the melt pool shape [53] due to which it was necessary to consider the effect of surface tension as it was responsible for modifying the pressure on the melt and thus affecting the depth of the machined cavity. The laser beam gets defocused with the change in the depth of the machined cavity and the laser power density is reduced due to the increasing distance of the material surface from the focal plane [27] and the effective beam radius is given by [27,54] 



where M<sup>2</sup> is the beam quality parameter assumed to be 1 for a perfect gaussian beam profile, df is the focal length of 120 mm, l is the laser wavelength of 1064 nm and zava is the available melt depth explained earlier. Beam quality factor represents the beam 



<!-- Start of picture text -->
Laser Machining of Alumina<br>Laser Parameters (power, pulse width, beam radius, repetition rate)<br>Materialplate thickness)properties and dimensions (density, specific heat, thermal conductivity, heat transfer coefficient,<br>Initial conditions (initial expetied depth (ca)= initial depth of hole (he) = 0, inital temperature =300K)<br>3D thermal model (Eqns. 1-3)-> Temperature after first pulse<br>ITi,Ti' (Eqns. 4-5) > Heating curve & Melt depth from surface 2<br>Eqn. 8 > Evaporation losses Zeva<br>Eqn. 9 > Drop in<br>temperature AT eva<br>fEqn.10 >Recoil pressure, pe<br>Available melt depth Zava<br>Egn.11 >Effective beam radius, rert<br>Egn.12 Expulsion velocity, Vexo<br>Eqn.14 >Expelled depth, &<br>Eqn 15 Depth of machined cavity,h<br>is required machined depth reached?<br>(Obtain actual number of pulses required for machining required depth<br><!-- End of picture text -->

Fig. 6. Flowchart showing procedure for prediction of machined depth. 

A.N. Samant, N.B. Dahotre / International Journal of Machine Tools & Manufacture 48 (2008) 1345–1353 

1351 

quality which is a measure of the focusability of the laser used. It was assumed in this study that the beam is initially at full focus, thus corresponding to a beam quality factor of 1. Attempts are ongoing to accurately determine M<sup>2</sup> and it will be incorporated in due course of time. Incorporation of actual M<sup>2</sup> values will take into account the complex distribution of energy taking place during the laser machining process. However, currently, the effect of the defocusing of the laser beam was accounted for by using the effective beam radius (Eq. (11) above). The surface tension pressure depends on this effective beam radius [50] and the melt available at the axis of the beam was expelled with a velocity vexp given by [50] 1 <u>pe</u> � <u>b=reff</u> vexpðtÞ ¼ ~~se~~ t (12) r reff 





where o ¼ 6 � woo 10<sup>�5</sup> K<sup>�1</sup> is the surface tension temperature coefficient [55], reff is the effective beam radius determined above in Eq. (11) and t is the time. As the temperature reached after the first few pulses is less than the melting point of alumina, there will be no material expulsion. Hence, the expression for expulsion velocity (Eq. (12)) above does not imply for the first few pulses which are responsible for just raising the temperature of the material till the melting point is reached, after which the material expulsion process begins as governed by Eq. (12). Where as in case of through the depth machining, during application of final pulses, as explained later, only a very thin layer of the material remains which is simply pushed down from bottom by the recoil pressure. Eq. (12), therefore, does not apply to the later set of pulses during machining of a through cavity (hole). Instead, the expression is only applied for the range of pulses where the material removal mechanism remains the same and is through expulsion. Integration of the expelled velocity over time (Eq. (14)) gave the fraction of the effective melt depth that was expelled at a certain time instant, dt, and the depth of machined cavity ht was given by Eq. (15) [56] 





The flow chart for attaining the final machined depth using the process parameters and material properties is presented in Fig. 6 and the computational predictions of temporal evolution of cavity machined (for 100% energy absorption) along with the schematic of different stages of cavity formation are represented in Fig. 7a and b, respectively. 

The temporal evolution of the depth of the machined cavity for a given material thickness depends on the interaction time, i.e. the number of pulses to which the material is exposed because it governs the amount of energy going into the material. Hence, the evolution profile is different for different number of pulses. From this profile (Fig. 7a), comparison between experimental and predicted number of pulses and the time required for machining a certain depth of material was made in Table 2 for different absorptivity values (0.8, 0.9 and 1.0). The predicted number of pulses/machining time for absorptivity values of 0.8 and 0.9 were similar because at these two absorptivity values, the rise in temperature due to increase in input laser energy was compensated by the drop in temperature due to evaporation, thus yielding similar surface temperatures for both the cases. Hence, no significant effect was seen on the predicted number of pulses/ machining time because the expulsion velocity and the machined 



<!-- Start of picture text -->
a<br>4 ty<br>—E —5 pulses '1<br>Es +--+ 10 pulses ts H<br>a ——20 pulses f 1<br>= —— 30 pulses \ ;<br>§ 2 Gmnami]\/ |<br>9<br>£d 1<br>" t L ' ;<br>J , i t<br>C) 02 04 0.6 08 1<br>Time (sec)<br>b Incident laser beam<br>Machined cavity<br>Expelled melt<br>Piste Melt depth _ Tye<br>thickness Unexpelled SS<br>melt<br>77 rine te<br><!-- End of picture text -->

Fig. 7. Temporal evolution of machined depth during laser machining of ceramic: (a) computational predictions (for 100% absorption) and (b) schematic for progression of cavity formation. 

Table 2 

Comparison between number of pulses for a particular depth of machined cavity for different absorptivity values 

|Depth of|Pulsesexperimental|Pulsesmodel|Pulsesmodel|
|---|---|---|---|
|machined|(time, s)|(a¼0.8, 0.9)|(a¼1.0)|
|cavity (mm)||(time, s)|(time, s)|
|0.26|5 (0.25)|4 (0.24)|3 (0.15)|
|0.56|10 (0.5)|9 (0.49)|7 (0.35)|
|3.23|20 (1.0)|20 (1.0)|16 (0.8)|
|4.0|30 (1.5)|24 (1.2)|19 (0.94)|



depth were a function of the surface temperature (Eqs. (9)–(15) above). 

It can also be seen from Table 2 that the number of pulses predicted from the model for absorptivity of 1.0 (considering multiple reflection phenomena) were less than those predicted by considering theoretical absorptivity value of 0.8 and 0.9. This could be attributed to the fact that when 100% energy absorption was considered, more energy was input to the material in the same amount of time thus machining more material in a shorter time. However, for all the absorptivity values considered in the present study, the predicted number of pulses was close to those actually required to machine depths of 0.26, 0.56, 3.23 and 4.0 mm. The predicted number of pulses was less than those 

A.N. Samant, N.B. Dahotre / International Journal of Machine Tools & Manufacture 48 (2008) 1345–1353 

1352 

experimentally detected for machining because the number of pulses were chosen based on prior experience in laser processing and hence the material could have been exposed to few extra pulses even after the desired depth of the material was machined. Some error could also have been introduced while measuring the machined depth from the micrographs (Fig. 1). In addition to the above considered physical phenomena, there could be some other mechanisms which are not incorporated in this study that could have had an effect on the predicted number of pulses. Thus the presented model can assist to determine the number of pulses required for machining a certain depth in a given material under a certain set of other laser parameters. 

The recoil pressure expelled the material in the upward direction and continued to do so for increased depth of machined cavity till around time instant t2. (Fig. 7b) At around time instant t3, when a very thin layer of the material remained in the bottom, the recoil pressure was able to push most of the material in the downward direction due to which the direction of material expulsion was reversed in the final stages of machining. In case of through depth machining, such reversal in material expulsion was because of minimum resistance to the recoil pressure by the small mass of supporting material at the bottom. Finally, all the rest of molten material was expelled and a clean through cavity was formed passing through the entire thickness of the material at around time instant t4. Thus the prediction of exact number of pulses to machine a required depth in a given type of material under chosen set of laser processing parameters would be extremely advantageous to save significant amount of energy and time. Although in this work, other than the number of pulses all laser machining parameters were kept constant, because of their interdependence, the present computational model can be configured to predict these parameters under various combinations of processing. 

## 4. Conclusion 

Machining of different depths of alumina ceramic was successfully carried out using pulsed laser, thus demonstrating the capabilities of lasers in machining ceramics. Multiple reflections within the high aspect ratio machined cavities were responsible for increasing the amount of energy absorbed. The thermal effects were responsible for melting and evaporating the material while the recoil pressure and surface tension was responsible to expel the molten material to machine a cavity of desired depth. All these effects were integrated in a computational model and the predictions were compared with experimentally detected pulses for machining different depths of alumina disc which showed a reasonable match, thus proving the model’s efficiency in foreseeing the number of pulses required for machining desired depth in a material. It was found that for increase in energy absorption from 80–90% to 100% (due to multiple reflections) by the alumina ceramic, the number of pulses required to machine depths of 0.26, 0.56, 3.23 and 4.0 mm reduced to 4, 9, 20, 24 and 3, 7, 16, 19 pulses, respectively, which were less than the number of pulses experimentally determined (5, 10, 20, and 30, respectively) to machine the same depths. 

Such a comprehensive approach differentiated the current work from earlier work such as that of Miyazaki et al. [57] and Salonitis et al. [27] who considered the drilling mechanism as comprised of melting and subsequent material removal by melt expulsion where as Atanasov et al. [58] considered the drilling of alumina merely by a single-step material evaporation without any melting. On the contrary, in the present study, the material removal during the drilling process takes place due to a combination of melt expulsion and evaporation processes. 

Furthermore, the past studies [27,57,58] have also neglected the effect of multiple reflections on the absorbed laser energy which, has a subsequent effect on the predicted number of pulses as seen in the present study. Thus, the systematic approach considered in this study is an advancement of the existing computational approach to drilling/machining of ceramics. 

## References 

- [1] R.W. Davidge, Mechanical Behavior of Ceramics, Cambridge University Press, Cambridge, 1979. 

- [2] T. Warren Liao, Flexural strength of creep feed ground ceramics: general pattern, ductile–brittle transition and MLP modeling, International Journal of Machine Tools & Manufacturing 38 (4) (1998) 257–275. 

- [3] S. Reschke, C. Bogdanow, Engineering ceramics: new perspectives through value-added (multi-) functionality, Key Engineering Materials 175–176 (1999) 1–10. 

- [4] Q.H. Zhang, J.H. Zhang, D.M. Sun, G.D. Wang, Study on the diamond tool drilling of engineering ceramics, Journal of Materials Processing Technology 122 (2002) 232–236. 

- [5] C. Tsutsumi, K. Okano, T. Suto, High quality machining of ceramics, Journal of Materials Processing Technology 37 (1993) 639–654. 

- [6] C.W. Chang, C.P. Kuo, An investigation of laser-assisted machining of Al2O3 ceramics planning, International Journal of Machine Tools & Manufacture 47 (2007) 452–461. 

- [7] R.L. Allor, S. Jahanmir, Current problems and future directions for ceramic machining, Journal of the American Ceramic Society Bulletin 75 (7) (1996) 40–43. 

- [8] J.Y. Shen, C.B. Luo, W.M. Zeng, X.P. Xu, Y.S. Gao, Ceramics grinding under the condition of constant pressure, Journal of Materials Processing Technology 129 (2002) 176–181. 

- [9] W. Konig, A. Wagemann, Machining of ceramic components: process—technological potentials, Machining of Advanced Materials, NIST Special Publication 847 (1990) 3–16. 

- [10] G. Chryssolouris, N. Anifantis, S. Karagiannis, Laser assisted machining: an overview, Journal of Manufacturing Science and Engineering, ASME 119 (1997) 766–769. 

- [11] B.G. Koepke, R.J. Stokes, A study of grinding damage in magnesium oxide single crystals, Journal of Materials Science 5 (1970) 240–247. 

- [12] H.P. Kirchner, Damage penetration at elongated machining grooves in hotpressed Si3N4, Journal of the American Ceramic Society 67 (5) (1984) 127–132. 

- [13] J.C. Conway, H.P. Kirchner, Crack branching as a mechanism of crushing during grinding, Journal of the American Ceramic Society 69 (1986) 603–607. 

- [14] H.K. Xu, S. Jahanmir, Microfracture and material removal in scratching of alumina, Journal of Materials Science 30 (1995) 2235–2247. 

- [15] B. Zhang, Precision grinding regime of advanced ceramics, in: Proceedings of the 1993 Annual Meeting of American Society of Precision Engineering, Seattle, Washington, DC, November 7–12, 1993, pp. 225–229. 

- [16] B. Zhang, T.D. Howes, Material removal mechanisms in grinding ceramics, Annals of CIRP 43 (1994) 305–308. 

- [17] B. Zhang, X.L. Zheng, H. Tokura, M. Yoshikawa, Grinding induced damage in ceramics, Journal of Materials Processing Technology 132 (2003) 353–364. 

- [18] J.P. Choi, B.H. Jeon, B.H. Kim, Chemical-assisted ultrasonic machining of glass, Journal of Materials Processing Technology 191 (2007) 153–156. 

- [19] I. Puertas, C.J. Luis, A study on the electrical discharge machining of conductive ceramics, Journal of Materials Processing Technology 153–154 (2004) 1033–1038. 

- [20] S.K. Chak, P.V. Rao, Trepanning of Al2O3 by electro-chemical discharge machining (ECDM) process using abrasive electrode with pulsed DC supply, International Journal of Machine Tools & Manufacture 47 (2007) 2061–2070. 

- [21] A.S. Kuar, B. Doloi, B. Bhattacharyya, Modelling and analysis of pulsed Nd:YAG laser machining characteristics during micro-drilling of zirconia (ZrO2), International Journal of Machine Tools & Manufacture 46 (2006) 1301–1310. 

- [22] C. Bagger, F.O. Olsen, Pulsed mode laser cutting of sheets for tailored blank, Journal of Materials Processing Technology 115 (2001) 131–135. 

- [23] D.K.Y. Low, L. Li, P.J. Byrd, Spatter prevention during the laser drilling of selected aerospace materials, Journal of Materials Processing Technology 139 (2003) 71–76. 

- [24] X. Yahong Liang, S.P. Dutta, Application trend in advanced ceramic technologies, Technovation 21 (2001) 61–65. 

- [25] W. Perrie, A. Rushton, M. Gill, P. Fox, W. O’Neill, Femtosecond laser microstructuring of alumina ceramic, Applied Surface Science 248 (2005) 213–217. 

- [26] C. Barnes, P. Shrotriya, P. Molian, Water-assisted laser thermal shock machining of alumina, International Journal of Machine Tools & Manufacture 47 (2007) 1864–1874. 

- [27] K. Salonitis, A. Stournaras, G. Tsoukantas, P. Stavropoulos, G. Chryssolouris, A theoretical and experimental investigation on limitations of pulsed laser drilling, Journal of Materials Processing Technology 183 (2007) 96–103. 

- [28] J.G. Andrews, D.R. Atthey, Hydrodynamic limit to penetration of a material by a high-power beam, Journal of Physics D—Applied Physics 9 (1976) 2181–2194. 

A.N. Samant, N.B. Dahotre / International Journal of Machine Tools & Manufacture 48 (2008) 1345–1353 

1353 

- [29] M.F. Modest, H. Abakian, Heat conduction in a moving semi-infinite solid subjected to pulsed laser irradiation, ASME Journal of Heat Transfer 108 (1986) 602–607. 

- [30] M.F. Modest, H. Abakian, Evaporative cutting of a semi-infinite body with a moving CW laser, ASME Journal of Heat Transfer 108 (1986) 597–601. 

- [31] H. Abakian, M.F. Modest, Evaporative cutting of a semi-transparent body with a moving CW laser, ASME Journal of Heat Transfer 110 (1988) 924–930. 

- [32] M. Modest, Laser machining of ablating/decomposing materials through cutting and drilling models, Journal of Laser Applications 9 (1997) 137–145. 

- [33] S.P. Harimkar, A.N. Samant, N.B. Dahotre, Temporally evolved recoil pressure driven melt infiltration during laser surface modifications of porous alumina ceramic, Journal of Applied Physics 101 (2007) 054911. 

- [34] W.H. Gitzen, Alumina as a Ceramic Material, The American Ceramic Society, Westerville, OH, 1970. 

- [35] Y.S. Touloukian, Thermophysical Properties of High Temperature Materials, IFI/Plenum, New York, 1967. 

- [36] H. Ki, P.S. Mohanty, J. Mazumder, Multiple reflection and its influence on keyhole evolution, Journal of Laser Applications 14 (2002) 39–45. 

- [37] K. Minamida, H. Takafuji, N. Hamada, H. Haga, N. Mizuhashi, Wedge shape welding with multiple reflection effects of high power CO2 laser beam, in: Fifth International Congress on Applications of Lasers and Electro-optics, 1986, pp. 97–104. 

- [38] F.A. Rahman, K. Takahashi, C.H. Teik, Theoretical analysis of coupling between laser diodes and conically lensed single-mode fibres utilizing ABCD matrix method, Optics Communications 215 (2003) 61–68. 

- [39] S.Y. Bang, S. Roy, M.F. Modest, CW Laser machining of hard ceramics—II. Effect of multiple reflections, International Journal of Heat and Mass Transfer 36 (1993) 3529–3540. 

- [40] M.F. Modest, Effect of multiple reflections on hole formation during short pulsed laser drilling, Journal of Heat Transfer 128 (2006) 653–661. 

- [41] A.W. Baily, A. Modak, Numerical simulation of laser ablation with cavity reflections, Journal of Thermophysics and Heat Transfer 3 (1989) 42–45. 

- [42] S.Y. Bang, M.F. Modest, Multiple reflection effects on evaporative cutting with a moving CW laser, Journal of Heat Transfer 113 (1991) 663–669. 

- [43] J.G. Andrews, D.R. Atthey, Hydrodynamic limit to penetration of a material by a high-power beam, Journal of Physics D—Applied Physics 9 (1976) 2181–2194. 

- [44] J. Mazumdar, W.M. Steen, Heat transfer model for CW laser material processing, Journal of Applied Physics 51 (1980). 

- [45] F.P. Incropera, D.P. Dewitt, Fundamentals of Heat and Mass Transfer, Wiley, New York, 2002. 

- [46] B. Bhushan, B. Gupta, Handbook of Tribology (Materials, Coatings and Surface Treatments), McGraw-Hill, New York, 1991. 

- [47] P.V. Ananthapadmanabhan, T.K. Thiyagarajan, K.P. Sreekumar, N. Venkatramani, Formation of nano-sized alumina by in-flight oxidation of aluminium powder in a thermal plasma reactor, Scripta Materialia 50 (2004) 143–147. 

- [48] M. Baker, MSDS. Aluminum Oxide: Material Safety Data Sheet 

- [49] M.V. Allmen, P. Blaser, K. Affolter, E. Strumer, Absorption phenomena in metal drilling with Nd-lasers, IEEE Journal of Quantum Electronics 14 (1978) 85–88. 

- [50] A. Matsunawa, V. Semak, The simulation of front keyhole wall dynamics during laser welding, Journal of Physics D—Applied Physics 30 (1997) 798–809. 

- [51] V. Semak, A. Matsunawa, The role of recoil pressure in energy balance during laser materials processing, Journal of Physics D—Applied Physics 30 (1997) 2541–2552. 

- [52] S.I. Anisimov, Vaporization of metal absorbing laser radiation, Soviet Physics JETP 27 (1968) 182–183. 

- [53] L. Han, F.W. Liou, S. Musti, Thermal behavior and geometry model of melt pool in laser material process, Journal of Heat Transfer 127 (2005) 1005–1014. 

- [54] H. Kogelnik, T. Li, Laser beams and resonators, Applied Optics 5 (1956) 1550–1565. 

- [55] B. Glorieux, F. Millot, J.C. Rifflet, Surface tension of liquid alumina from contactless techniques, International Journal of Thermophysics 23 (2002) 1249–1257. 

- [56] V.V. Semak, G.A. Knorovsky, D.O. MacCallum, R.A. Roach, Effect of surface tension on melt pool dynamics during laser pulse interaction, Journal of Physics D—Applied Physics 39 (2006) 590–595. 

- [57] T. Miyazaki, S. Yoshioka, T. Kimura, Ejection of molten material produced by pulsed electron and laser beams, Precision Engineering 10 (1988) 141–146. 

- [58] P.A. Atanasov, E.D. Eugenieva, N.N. Nedialkov, Laser drilling of silicon nitride and alumina ceramics: a numerical and experimental study, Journal of Applied Physics 89 (2001). 

