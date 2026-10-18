# Rod and piston sources for the concept H stack (read 2026-10-18)

Source record for `analysis/engine_crank/stack_h.py` and section 9 of `CASTINGS_H.md` (AER-3442). Every value was read on 2026-10-18 from the URL given. "Snippet" means the value came from a search-result summary and the page itself could not be loaded to confirm it. "Not found" means not found; it is not an estimate.

## What was looked for and not found

**A catalog drawing of an LS rod's big end, or of an LS piston's skirt and pin bosses.** Looked for in the Callies 2022 catalog, the K1 2015 catalog, Manley's rod page, the MAHLE LS7 piston sheet, and the JE, Wiseco, Diamond and CP product pages. None of them publishes an outline, a cap-screw spacing, a big-end swing radius, a skirt length, a pin-to-skirt dimension or a boss depth. The vendors publish only the fit dimensions listed below. JE's and Wiseco's product pages returned HTTP 403 to the fetch tool, and Wiseco's 60419X125 page loaded with no skirt dimension on it.

## Rods, 2.100 in journal

| Item | Value | Source | Note |
|---|---|---|---|
| Callies LS Ultra H-Beam | 6.100 / 6.125 / 6.200 / 6.350 / **6.460** in, 2.100 in journal; U16290 / U16300 / U16303 / U16302 / **U16301**; 620 / 649 / 625 / 658 / **661 g** | https://www.callies.com/wp-content/uploads/2021/12/2022Catalog-With-Covers.pdf (p. 18) | crank_decision.py had 6.460 in as "not found"; it is a catalog length |
| Callies LS Ultra I-Beam | 6.350 in, 2.100 in, U17178, 674 g | same, p. 18 | |
| Callies LS Compstar H-Beam | **6.560 in, 2.100 in, CSC6560DS2A2AH, 655 g**; also 6.340 and 6.440 in on a 2.000 in journal | same, p. 18 | the catalog row gives no pin size; CSC6125DS2A2AH is listed with a 0.927 in pin by Mullins, and CSC6100DS6A2AH carries a ".943 pin" note, so "S2" reads as 0.927 in [E, from the code] |
| Callies Compstar CSC6125DS2A2AH | 6.125 in, 2.100 in, 0.927 in pin; 0.940 in big-end width; 7/16 in ARP2000 cap screws | https://mullinsraceparts.com/product/callies-performance-products-compstar-connecting-rods-ls1-6-125-length-x-2-100-rod-journal-927-wrist-pin-single-connecting-rod/ | snippet |
| K1 LS rod | 6.125 in; big-end bore 2.225 in; pin bore 0.927 in; big-end width 0.940 in; 7/16 in bolts | https://www.msprodimages.com/PDFCatalogs/PGPCatalog/K1T_K1_Technology_2015.pdf | snippet; the PDF loaded but the rod page did not extract |
| Molnar GM LS H-beam | 6.125 in, 2.100 in, 0.940 in big-end width, 7/16 in ARP2000 | https://molnarrods.com/gm-ls-connecting-rods | snippet |
| Lunati / Scat LS | 6.125 in, 2.100 in, 0.927 in pin, 0.940 in big-end width | https://Jegs.com/p/Manley/Manley-Chevrolet-LS-H-Lite-Series-H-Beam-Connecting-Rods/3318946/10002/-1 ; https://tre.dev.webshopmanager.com/product/scat-stroker-pro-sport-4340-forged-h-beam-connecting-rods-for-gen-1-sbc-ls-lt-engines-6-125-length-2-100-rod-journal | snippets |
| LS cap-screw spacing, big-end outline | **not found** | | |

## Pistons, 4.125 in (104.8 mm) bore, 0.927 in pin

| Item | Value | Source | Note |
|---|---|---|---|
| MAHLE 930221525 | LS7, 4.125 in, 4.000 in stroke, 6.067 in rod, **CH 1.181 in**, 0.927 in pin, -2.5 cc, 447 g, 4032; rings 1.0 / 1.0 / 2.0 mm | https://www.mahle.com/media/usa/motorsports/ls7-flat-top-&-dish-webpage.pdf | read from the PDF's text layer |
| MAHLE 930221625 | LS7, 4.125 in, 4.000 in stroke, 6.125 in rod, **CH 1.105 in**, 0.927 in pin, -2.5 cc, **438 g**, 4032 | same | the piston stack_h.py picks |
| Wiseco 60419X125 | 4.125 in, CH 1.165 in, -23 cc, 2618, 0.927 in H13 pin; $165.99 each ($183.95 MSRP) | https://auto.wiseco.com/60419x125 | verified on the page; no skirt dimension listed |
| JE / CP LS7 pins | 0.927 x 2.250 in | https://www.jegs.com/i/je-pistons-532-324038-324038-piston-set-chevrolet-ls-inv-dome-dish-4-135-bore-1-165-cd-0-927-pin-set-of-8 ; https://cnc-motorsports.com/catalog/product/view/_ignore_category/1/id/80292/s/bls1204-std-cp-pistons-bullet-ls7-12-forged-4-125-bore-11-1-1/ | snippets |
| LS piston skirt length, pin-to-skirt, boss depth | **not found** | | |
