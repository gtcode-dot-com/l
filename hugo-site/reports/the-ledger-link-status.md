# The Ledger Link Status Report

Checked: 2026-03-04 14:00

Method: `curl -L --connect-timeout 5 --max-time 8` for external URLs; `curl` against `http://localhost:1313` for archival copies.

## External URLs

| URL | Status | Effective URL | Notes |
|---|---|---|---|
| https://www.irs.gov/instructions/i990sf | 200 | https://www.irs.gov/instructions/i990sf |  |
| https://www.irs.gov/instructions/i990si | 200 | https://www.irs.gov/instructions/i990si |  |
| https://www.irs.gov/instructions/i990sb | 200 | https://www.irs.gov/instructions/i990sb |  |
| https://www.justice.gov/nsd-fara | 200 | https://www.justice.gov/nsd-fara |  |
| https://hbe.ehawaii.gov/documents/business.html?fileNumber=3923D2 | 200 | https://hbe.ehawaii.gov/documents/business.html;jsessionid=60B9FBAE7F056AA5940604092A602964.app8?fileNumber=3923D2 |  |
| https://projects.propublica.org/nonprofits/organizations/990035507 | 200 | https://projects.propublica.org/nonprofits/organizations/990035507 |  |
| https://www.hawaiinewsnow.com/2024/01/30/chinese-chamber-commerce-hawaiis-returns-china-first-trip-since-pandemic/ | 200 | https://www.hawaiinewsnow.com/2024/01/30/chinese-chamber-commerce-hawaiis-returns-china-first-trip-since-pandemic/ |  |
| https://www.hawaiinewsnow.com/2024/03/17/top-official-chinas-fujian-province-hawaii-goodwill-visit/ | 200 | https://www.hawaiinewsnow.com/2024/03/17/top-official-chinas-fujian-province-hawaii-goodwill-visit/ |  |
| https://www.fujian.gov.cn/english/news/202403/t20240328_6420989.htm | 200 | https://www.fujian.gov.cn/english/news/202403/t20240328_6420989.htm |  |
| http://usa.chinadaily.com.cn/epaper/2011-11/14/content_14092246.htm | 200 | http://usa.chinadaily.com.cn/epaper/2011-11/14/content_14092246.htm |  |
| https://lfestorage.s3.us-east-2.amazonaws.com/lfe/pdf/China-USASymposium.pdf | 200 | https://lfestorage.s3.us-east-2.amazonaws.com/lfe/pdf/China-USASymposium.pdf | Large PDF; download timed out during check but returned 200. |
| https://www.caifc.org.cn/index.php?m=content&c=index&a=show&catid=41&id=924 | ERR |  | Timeout during check. |
| https://www.gofundme.com/f/help-needed-for-a-chemical-attack-victim | 200 | https://www.gofundme.com/f/help-needed-for-a-chemical-attack-victim |  |
| https://files.hawaii.gov/dbedt/annuals/2024/2024-bdsd-overseas.pdf | 404 | https://files.hawaii.gov/dbedt/annuals/2024/2024-bdsd-overseas.pdf | Archived via Wayback. |
| https://hbe.ehawaii.gov/annuals/rest/annuals/3923D2/status | 200 | https://hbe.ehawaii.gov/annuals/rest/annuals/3923D2/status |  |
| https://projects.propublica.org/nonprofits/api/v2/organizations/990035507.json | 200 | https://projects.propublica.org/nonprofits/api/v2/organizations/990035507.json |  |

## Archival Copies (localhost)

| Path | Status |
|---|---|
| /sources/the-ledger/IRS_ScheduleF_Instructions.html | 200 |
| /sources/the-ledger/IRS_ScheduleI_Instructions.html | 200 |
| /sources/the-ledger/IRS_ScheduleB_Instructions.html | 200 |
| /sources/the-ledger/DOJ_FARA_Overview.html | 200 |
| /sources/the-ledger/DCCA_CCCH_Standing.html | 200 |
| /sources/the-ledger/irs-990/ccch_202112259349302141.xml | 200 |
| /sources/the-ledger/irs-990/ccch_202242389349301109.xml | 200 |
| /sources/the-ledger/irs-990/ccch_202322099349301702.xml | 200 |
| /sources/the-ledger/irs-990/ccch_202422289349304212.xml | 200 |
| /sources/the-ledger/irs-990/ccch_202502349349301340.xml | 200 |
| /sources/the-ledger/HawaiiNewsNow_Chamber_China_Jan2024.html | 200 |
| /sources/the-ledger/HawaiiNewsNow_Fujian_Mar2024.html | 200 |
| /sources/the-ledger/Fujian_Gov_GuoNingning_Hawaii_2024.html | 200 |
| /sources/the-ledger/ChinaDaily_CCCH_2011.html | 200 |
| /sources/the-ledger/CCCH_CAIFC_Symposium_2010_Program.pdf | 200 |
| /sources/the-ledger/CAIFC_Narcissus_Diaoyutai_2018.html | 200 |
| /sources/the-ledger/GoFundMe_ChemicalAttack_2024.html | 200 |
| /sources/the-ledger/DBEDT_BDSD_Overseas_2024.pdf | 200 |
| /sources/the-ledger/DCCA_Annuals_Status_3923D2.json | 200 |
| /sources/the-ledger/ProPublica_CCCH_990.json | 200 |
| /sources/the-ledger/DBEDT_Fujian.html | 200 |
| /sources/the-ledger/DBEDT_Guo.html | 200 |
| /sources/the-ledger/Honolulu_Fujian.html | 200 |
| /sources/the-ledger/Honolulu_Guo.html | 200 |
| /sources/the-ledger/Honolulu_MOU.html | 200 |
| /sources/the-ledger/DCCA_Search_HFBA.html | 200 |
| /sources/the-ledger/DCCA_Search_HFFA.html | 200 |
| /sources/the-ledger/FARA_Registrants_Active.json | 200 |
| /sources/the-ledger/FARA_Registrants_Terminated.json | 200 |
| /sources/the-ledger/lda/LDA_registrant_ccch.json | 200 |
| /sources/the-ledger/lda/LDA_client_ccch.json | 200 |
| /sources/the-ledger/lda/LDA_registrant_ccch_abbrev.json | 200 |
| /sources/the-ledger/lda/LDA_client_ccch_abbrev.json | 200 |
| /sources/the-ledger/lda/LDA_registrant_warren_luke.json | 200 |
| /sources/the-ledger/lda/LDA_client_warren_luke.json | 200 |
