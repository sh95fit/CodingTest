with patient_apnt as (
    select a.APNT_NO, p.PT_NAME, p.PT_NO, a.MCDP_CD, a.APNT_YMD, a.MDDR_ID, a.APNT_CNCL_YN FROM PATIENT as p
    join APPOINTMENT as a ON a.PT_NO = p.PT_NO
)
select pa.APNT_NO, pa.PT_NAME, pa.PT_NO, pa.MCDP_CD, d.DR_NAME, pa.APNT_YMD from patient_apnt pa
join doctor as d on d.DR_ID = pa.MDDR_ID
WHERE pa.MCDP_CD = "CS" and DATE(pa.APNT_YMD) = "2022-04-13" and pa.APNT_CNCL_YN = "N"
ORDER BY pa.APNT_YMD