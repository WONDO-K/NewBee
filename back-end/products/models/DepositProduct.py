from django.db import models
from .bank import Bank

class DepositProduct(models.Model): # 정기 예금 상품
    fin_prdt_cd = models.CharField(max_length=40, unique=True)  # 금융상품 코드
    fin_co_no = models.ForeignKey(Bank, on_delete=models.CASCADE)  # 금융회사 코드
    kor_co_nm = models.CharField(max_length=100)  # 금융회사명
    fin_prdt_nm = models.CharField(max_length=100)  # 금융 상품명
    join_way = models.CharField(max_length=200)  # 가입 방법
    mtrt_int = models.TextField()  # 만기 후 이자율
    spcl_cnd = models.TextField()  # 우대조건
    join_deny = models.CharField(max_length=20)  # 가입제한
    join_member = models.CharField(max_length=100)  # 가입대상
    etc_note = models.TextField()  # 기타 유의사항
    max_limit = models.IntegerField(null=True, blank=True)  # 최고한도
    dcls_strt_day = models.CharField(max_length=10)  # 공시 시작일[YYYY-MM-DD]
    dcls_end_day = models.CharField(max_length=10,null=True, blank=True)  # 공시 종료일
    dcls_month = models.CharField(max_length=6)  # 공시 제출월 [YYYYMM]
    fin_co_subm_day = models.CharField(max_length=20)  # 금융회사 제출일 [YYYYMMDDHH24MI]

    def __str__(self):
        return self.fin_prdt_nm     
    
class DepositProductOption(models.Model): # 정기 예금 상품 옵션
    deposit_product = models.ForeignKey(DepositProduct, related_name='deposit_options', on_delete=models.CASCADE) # 정기 예금 상품, DepositProduct 실제 객체를 참조
    intr_rate_type = models.CharField(max_length=20) # 이자율 종류   
    intr_rate_type_nm = models.CharField(max_length=100) # 이자율 종류명
    save_trm = models.IntegerField() # 저축 기간
    intr_rate = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True) # 이자율
    intr_rate2 = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True) # 이자율2

    def __str__(self):
        return f"{self.deposit_product .fin_prdt_nm} - {self.intr_rate_type_nm}"
