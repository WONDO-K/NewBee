from rest_framework import serializers
from .models import Bank, BankOption, DepositProduct, DepositProductOption, SavingProduct, SavingProductOption, PensionProduct, PensionProductOption, RentLoanProduct, RentLoanProductOption


class BankOptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BankOption 
        fields = ['bank','area_cd','area_nm','exis_yn']
        read_only_fields = ['bank'] # bank 필드는 읽기 전용으로 설정

class BankSerializer(serializers.ModelSerializer):

    options = BankOptionSerializer(many=True, required=False)  # BankOptionSerializer 포함(역참조, 여러 개의 BankOption 객체를 시리얼라이즈)
    
    class Meta:
        model = Bank
        fields = ['id', 'fin_co_no', 'kor_co_nm', 'homp_url', 'cal_tel', 'options']
        read_only_fields = ['id'] # id 필드는 읽기 전용으로 설정

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProductOption
        fields = [
            'intr_rate_type', 'intr_rate_type_nm', 
            'save_trm', 'intr_rate', 'intr_rate2']

class DepositProductSerializer(serializers.ModelSerializer): 

    # related_name='deposit_options'로 지정한 필드명을 사용
    deposit_options = DepositOptionsSerializer(many=True,required=False)  # DepositProductOptionSerializer 포함(역참조, 여러 개의 DepositProductOption 객체를 시리얼라이즈)

    class Meta:
        model = DepositProduct
        fields = [
            'fin_prdt_cd','kor_co_nm', 'fin_prdt_nm', 
            'join_way', 'mtrt_int', 'spcl_cnd', 'join_deny', 'join_member', 
            'etc_note', 'max_limit', 'dcls_strt_day', 'dcls_end_day', 'dcls_month', 
            'fin_co_subm_day', 'deposit_options']

class SavingProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProductOption
        fields = [
            'intr_rate_type','intr_rate_type_nm','rsrv_type','rsrv_type_nm',
            'save_trm','intr_rate','intr_rate2']

class SavingProductSerializer(serializers.ModelSerializer):

    saving_options = SavingProductOptionSerializer(many=True,required=False)  # SavingProductOptionSerializer 포함(역참조, 여러 개의 SavingProductOption 객체를 시리얼라이즈)

    class Meta:
        model = SavingProduct
        fields = [
            'fin_prdt_cd', 'kor_co_nm', 'fin_prdt_nm', 
            'join_way', 'mtrt_int', 'spcl_cnd', 'join_deny', 'join_member', 
            'etc_note', 'max_limit', 'dcls_strt_day', 'dcls_end_day', 'dcls_month', 
            'fin_co_subm_day','saving_options']

class PensionProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PensionProductOption
        fields = [
            'dcls_month', 'fin_co_no', 'fin_prdt_cd', 'pnsn_recp_trm',
            'pnsn_recp_trm_nm', 'pnsn_entr_age', 'pnsn_entr_age_nm',
            'mon_paym_atm', 'mon_paym_atm_nm', 'paym_prd', 'paym_prd_nm',
            'pnsn_strt_age', 'pnsn_strt_age_nm', 'pnsn_recp_amt'
        ]
        
class PensionProductSerializer(serializers.ModelSerializer):

    pension_options = PensionProductOptionSerializer(many=True,required=False,read_only=True)

    class Meta:
        model = PensionProduct
        fields = [
            'dcls_month', 'fin_co_no', 'kor_co_nm', 'fin_prdt_cd', 
            'fin_prdt_nm', 'join_way', 'pnsn_kind', 'pnsn_kind_nm', 
            'sale_strt_day', 'mntn_cnt', 'prdt_type', 'prdt_type_nm', 
            'dcls_rate', 'guar_rate', 'btrm_prft_rate_1', 'btrm_prft_rate_2', 
            'btrm_prft_rate_3', 'etc', 'sale_co', 'dcls_strt_day', 
            'dcls_end_day', 'fin_co_subm_day', 'pension_options'
        ]

class RentLoanOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentLoanProductOption
        fields = [
            'dcls_month', 'fin_co_no', 'fin_prdt_cd', 'rpay_type', 
            'rpay_type_nm', 'lend_rate_type', 'lend_rate_type_nm', 
            'lend_rate_min', 'lend_rate_max', 'lend_rate_avg'
        ]

class RentLoanSerializer(serializers.ModelSerializer):
    rent_loan_options = RentLoanOptionSerializer(many=True, required=False, read_only=True)  # RentLoanOptionSerializer 포함(역참조)

    class Meta:
        model = RentLoanProduct
        fields = [
            'dcls_month', 'kor_co_nm', 'fin_prdt_cd', 
            'fin_prdt_nm', 'join_way', 'loan_inci_expn', 'erly_rpay_fee', 
            'dly_rate', 'loan_lmt', 'dcls_strt_day', 'dcls_end_day', 
            'fin_co_subm_day', 'rent_loan_options'
        ]

# 상품 리스트 조회 용 ----------------------------------------------------------------------------------------------------------------------------------------------------
# class ProductListSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ['fin_co_no','fin_prdt_cd','kor_co_nm','fin_prdt_nm',] 
    

# class SimpleDepositProductOptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DepositProductOption
#         fields = [
#             'intr_rate_type', 'intr_rate', 'intr_rate2'
#         ]

# class DepositListSerializer(ProductListSerializer):
#     deposit_options = SimpleDepositProductOptionSerializer(many=True, read_only=True)

#     class Meta(ProductListSerializer.Meta):
#         model = DepositProduct
#         fields = ProductListSerializer.Meta.fields + ['deposit_options']

# class SimpleSavingProductOptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SavingProductOption
#         fields = [
#             'intr_rate_type', 'rsrv_type', 'save_trm', 'intr_rate', 'intr_rate2'
#         ]
# class SavingListSerializer(ProductListSerializer):
#     saving_options = SimpleSavingProductOptionSerializer(many=True, read_only=True)

#     class Meta(ProductListSerializer.Meta):
#         model = SavingProduct
#         fields = ProductListSerializer.Meta.fields + ['saving_options']

# class SimplePensionProductOptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PensionProductOption
#         fields = [
#             'pnsn_recp_trm', 'pnsn_entr_age', 'mon_paym_atm', 'paym_prd', 'pnsn_strt_age', 'pnsn_recp_amt'
#         ]
# class PensionListSerializer(ProductListSerializer):
#     pension_options = SimplePensionProductOptionSerializer(many=True, read_only=True)

#     class Meta(ProductListSerializer.Meta):
#         model = PensionProduct
#         fields = ProductListSerializer.Meta.fields + ['pension_options']

# class SimpleRentLoanProductOptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RentLoanProductOption
#         fields = [
#             'rpay_type', 'lend_rate_type', 'lend_rate_min', 'lend_rate_max', 'lend_rate_avg'
#         ]
# class RentLoanListSerializer(ProductListSerializer):
#     rent_loan_options = SimpleRentLoanProductOptionSerializer(many=True, read_only=True)

#     class Meta(ProductListSerializer.Meta):
#         model = RentLoanProduct
#         fields = ProductListSerializer.Meta.fields + ['rent_loan_options']

from rest_framework import serializers

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['fin_co_no', 'fin_prdt_cd', 'kor_co_nm', 'fin_prdt_nm', 'pk']

class SimpleDepositProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProductOption
        fields = [
            'intr_rate_type', 'intr_rate', 'intr_rate2', 'pk']

class DepositListSerializer(ProductListSerializer):
    deposit_options = SimpleDepositProductOptionSerializer(many=True, read_only=True)

    class Meta(ProductListSerializer.Meta):
        model = DepositProduct
        fields = ProductListSerializer.Meta.fields + ['deposit_options']

class SimpleSavingProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProductOption
        fields = [
            'intr_rate_type', 'rsrv_type', 'save_trm', 'intr_rate', 'intr_rate2','pk'
        ]

class SavingListSerializer(ProductListSerializer):
    saving_options = SimpleSavingProductOptionSerializer(many=True, read_only=True)

    class Meta(ProductListSerializer.Meta):
        model = SavingProduct
        fields = ProductListSerializer.Meta.fields + ['saving_options']

class SimplePensionProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PensionProductOption
        fields = [
            'pnsn_recp_trm', 'pnsn_entr_age', 'mon_paym_atm', 'paym_prd', 'pnsn_strt_age', 'pnsn_recp_amt', 'pk'
        ]

class PensionListSerializer(ProductListSerializer):
    pension_options = SimplePensionProductOptionSerializer(many=True, read_only=True)

    class Meta(ProductListSerializer.Meta):
        model = PensionProduct
        fields = ProductListSerializer.Meta.fields + ['pension_options']

class SimpleRentLoanProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentLoanProductOption
        fields = [
            'rpay_type', 'lend_rate_type', 'lend_rate_min', 'lend_rate_max', 'lend_rate_avg', 'pk'
        ]

class RentLoanListSerializer(ProductListSerializer):
    rent_loan_options = SimpleRentLoanProductOptionSerializer(many=True, read_only=True)

    class Meta(ProductListSerializer.Meta):
        model = RentLoanProduct
        fields = ProductListSerializer.Meta.fields + ['rent_loan_options']



# 유저 상품 가입----------------------------------------------------------------------------------------------------------------------------------------------------

from .models import UserDepositProduct, UserSavingProduct, UserPensionProduct, UserRentLoanProduct
from django.conf import settings

class JoinProductSerializer(serializers.Serializer): # 사용자가 상품에 가입할 때 사용하는 시리얼라이저
    product_type = serializers.CharField(max_length=20) # 'deposit', 'saving', 'pension', 'rent_loan' 중 하나로 상품 타입을 의미
    product_id = serializers.IntegerField() # 상품 ID
    option_id = serializers.IntegerField() # 상품 옵션 ID


class UserProductSerializer(serializers.ModelSerializer):
    class Meta: # UserProductSerializer를 상속받는 Serializer 클래스에서 Meta 클래스를 정의할 때 상속받는 클래스의 Meta 클래스를 참조하도록 함
        fields = ['user', 'product_type', 'selected_option', 'join_date']


class UserDepositProductSerializer(UserProductSerializer):

    class Meta(UserProductSerializer.Meta):
        model = UserDepositProduct
        fields = UserProductSerializer.Meta.fields + ['deposit_product']

    def get_deposit_product(self, obj):
        return obj.deposit_product.fin_prdt_nm
    
class UserSavingProductSerializer(UserProductSerializer):

    class Meta(UserProductSerializer.Meta):
        model = UserSavingProduct
        fields = UserProductSerializer.Meta.fields + ['saving_product']

    def get_saving_product(self, obj):
        return obj.saving_product.fin_prdt_nm

class UserPensionProductSerializer(UserProductSerializer):

    class Meta(UserProductSerializer.Meta):
        model = UserPensionProduct
        fields = UserProductSerializer.Meta.fields + ['pension_product']

    def get_pension_product(self, obj):
        return obj.pension_product.fin_prdt_nm

class UserRentLoanProductSerializer(UserProductSerializer):

    class Meta(UserProductSerializer.Meta):
        model = UserRentLoanProduct
        fields = UserProductSerializer.Meta.fields + ['rent_loan_product']
    
    def get_rent_loan_product(self, obj):
        return obj.rent_loan_product.fin_prdt_nm


# 적금 수령액 계산용 ----------------------------------------------------------------------------------------------------------------------------------------------------

class CalcSavingSerializer(serializers.Serializer):
    product_pk = serializers.IntegerField(help_text="적금 상품의 ID를 입력하세요.")  # 적금 상품 ID
    option_pk = serializers.IntegerField(help_text="적금 상품 옵션의 ID를 입력하세요.")  # 적금 상품 옵션 ID
    principal = serializers.DecimalField(max_digits=10, decimal_places=2, help_text="투자한 원금을 입력하세요.")  # 원금
    n = serializers.IntegerField(default=1, help_text="복리 계산 시 연 단위 횟수를 입력하세요. (기본값 1)")  # 복리 계산 시 연 단위 횟수 (기본값 1)

    class Meta:
        fields = ['product_pk', 'option_pk', 'principal', 'n']