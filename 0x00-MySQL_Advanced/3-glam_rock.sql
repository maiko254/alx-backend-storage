-- mysql script that lists all bands in table metal_bands with Glam rock as their main style, ranked by their longevity (calculated from attributes formed and split)

SELECT band_name, IFNULL(split, 2022) - formed AS lifespan from metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC
