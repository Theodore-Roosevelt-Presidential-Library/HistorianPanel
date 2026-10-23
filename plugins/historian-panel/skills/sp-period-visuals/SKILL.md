---
name: sp-period-visuals
description: "Specialist for whether a picture of T.R.'s world looks right for its time and place — illustrations, AI-generated images, reenactment photos, video, animation, 3D reconstructions and exhibit graphics. Checks flags and star counts, uniforms and insignia, firearms, clothing, vehicles and technology, buildings, and what the landscape looked like then. Also enforces the Library's rule that image generators never depict identifiable buildings. Use before any new visual of a historical scene is published."
---

# Period accuracy of visuals

Read `reference/panel-rules.md` at the plugin root first.

## Scope

- Newly made visuals of historical scenes: illustrations, AI-generated images,
  reenactment and staged photographs, video and animation, 3D models and
  reconstructions, exhibit and map graphics.
- What they show: flags, uniforms, insignia, weapons, clothing, hair, vehicles,
  tools and technology, buildings, signage, plants and animals, and the
  landscape as it was then.
- The prompts and briefs used to make them.

## Out of scope

- Identifying who is in a historical photograph → `sp-photo-id`
- Dating historical film → `sp-film-sound-cartoons`
- Objects as artifacts (provenance, originals) → `sp-objects`
- Present-day photographs of the Library and sites, which are not historical
  scenes

## Where to look first

1. **Period photographs** of the same subject, found through holding
   institutions' catalogs (Library of Congress Prints & Photographs, Houghton,
   the Theodore Roosevelt Center, NPS museum collections). Compare the new
   visual with them. Hand identification questions to `sp-photo-id`.
2. **Reference works on flags:** the official star count for a given year
   comes from the history of the U.S. flag as published by government and
   museum sources (for example the Smithsonian's National Museum of American
   History). State the year the scene depicts and check the count for that year.
3. **Uniform and equipment references** from the U.S. Army Center of Military
   History and museum collections, for unit, rank and insignia by year.
4. **Material culture sources** through `sp-material-culture`: catalogs,
   advertisements and museum collections for clothing, vehicles and tools of
   the year.
5. **Landscape then vs. now:** period photographs, NPS historic resource
   studies, and land-cover records for what the Badlands, rivers and towns
   looked like at the time. Do not assume today's fences, roads, plants or
   wildlife populations were there.

## Known traps

- Flags with the wrong number of stars for the year shown. [method]
- Uniforms, insignia and rank marks from the wrong year, unit or service.
  [method]
- Modern objects in a period scene: zippers, plastic, paved roads, power lines,
  modern eyewear, later firearms. [method]
- Buildings invented by an image model. Generated images never depict an
  identifiable building, monument or named structure; use real photography for
  those. [house-rule]
- Landforms drawn as the wrong kind. North Dakota's are buttes, not mesas.
  [house-rule]
- T.R.'s appearance generalized from late-life images onto a younger man, or
  the reverse. Match his age in the scene. [method]
- Animals, plants or people placed where they were not, or in numbers that do
  not fit the year. [method]
- A reconstruction shown without saying it is one. Label reconstructions and
  illustrations as such. [method]

## Procedure

1. Name the scene: who, where, and the exact year or date it depicts.
2. List everything visible that has a period answer: flags, uniforms, weapons,
   clothing, vehicles, buildings, landscape, signage.
3. For each, find period evidence for that year and place.
4. For generated images, also read the prompt and check it contains the
   Library's no-buildings instruction.
5. Mark each element as correct, wrong (with what it should be), or unknown.
6. Recommend fixes, or a caption that labels the image as an illustration or
   reconstruction.

## Output

Follow reference/panel-rules.md section 11. Use one verdict per visible element
that was checked.
