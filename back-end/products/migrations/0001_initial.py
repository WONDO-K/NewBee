

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=6)),
                ('fin_co_no', models.CharField(max_length=20, unique=True)),
                ('kor_co_nm', models.CharField(max_length=100)),
                ('homp_url', models.URLField()),
                ('cal_tel', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DepositProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.CharField(max_length=40, unique=True)),
                ('kor_co_nm', models.CharField(max_length=100)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('join_way', models.CharField(max_length=200)),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.CharField(max_length=20)),
                ('join_member', models.CharField(max_length=100)),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField(blank=True, null=True)),
                ('dcls_strt_day', models.CharField(max_length=10)),
                ('dcls_end_day', models.CharField(blank=True, max_length=10, null=True)),
                ('dcls_month', models.CharField(max_length=6)),
                ('fin_co_subm_day', models.CharField(max_length=20)),
                ('fin_co_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.bank')),
            ],
        ),
        migrations.CreateModel(
            name='DepositProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intr_rate_type', models.CharField(max_length=20)),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('save_trm', models.IntegerField()),
                ('intr_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('intr_rate2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('deposit_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_options', to='products.depositproduct')),
            ],
        ),
        migrations.CreateModel(
            name='PensionProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=6)),
                ('fin_co_no', models.CharField(max_length=20)),
                ('kor_co_nm', models.CharField(max_length=100)),
                ('fin_prdt_cd', models.CharField(max_length=40)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('join_way', models.CharField(max_length=200)),
                ('pnsn_kind', models.CharField(max_length=20)),
                ('pnsn_kind_nm', models.CharField(max_length=100)),
                ('sale_strt_day', models.CharField(blank=True, max_length=10, null=True)),
                ('mntn_cnt', models.IntegerField()),
                ('prdt_type', models.CharField(max_length=20)),
                ('prdt_type_nm', models.CharField(max_length=100)),
                ('dcls_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('guar_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('btrm_prft_rate_1', models.DecimalField(decimal_places=2, max_digits=5)),
                ('btrm_prft_rate_2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('btrm_prft_rate_3', models.DecimalField(decimal_places=2, max_digits=5)),
                ('etc', models.TextField(blank=True, null=True)),
                ('sale_co', models.CharField(max_length=200)),
                ('dcls_strt_day', models.CharField(max_length=10)),
                ('dcls_end_day', models.CharField(blank=True, max_length=10, null=True)),
                ('fin_co_subm_day', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PensionProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=6, verbose_name='공시 제출월 [YYYYMM]')),
                ('fin_co_no', models.CharField(max_length=20, verbose_name='금융회사 코드')),
                ('fin_prdt_cd', models.CharField(max_length=20, verbose_name='금융상품 코드')),
                ('pnsn_recp_trm', models.CharField(max_length=20, verbose_name='연금수령기간')),
                ('pnsn_recp_trm_nm', models.CharField(max_length=100, verbose_name='연금수령기간명')),
                ('pnsn_entr_age', models.CharField(max_length=20, verbose_name='연금가입나이')),
                ('pnsn_entr_age_nm', models.CharField(max_length=100, verbose_name='연금가입나이명')),
                ('mon_paym_atm', models.CharField(max_length=20, verbose_name='월납입금액')),
                ('mon_paym_atm_nm', models.CharField(max_length=100, verbose_name='월납입금액명')),
                ('paym_prd', models.CharField(max_length=20, verbose_name='납입기간')),
                ('paym_prd_nm', models.CharField(max_length=100, verbose_name='납입기간명')),
                ('pnsn_strt_age', models.CharField(max_length=20, verbose_name='연금개시나이')),
                ('pnsn_strt_age_nm', models.CharField(max_length=100, verbose_name='연금개시나이명')),
                ('pnsn_recp_amt', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='연금수령금액')),
                ('pension_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pension_options', to='products.pensionproduct')),
            ],
            options={
                'verbose_name': '연금 상품 옵션',
                'verbose_name_plural': '연금 상품 옵션 목록',
            },
        ),
        migrations.CreateModel(
            name='RentLoanProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=6, verbose_name='공시 제출월 [YYYYMM]')),
                ('fin_prdt_cd', models.CharField(max_length=40, verbose_name='금융상품 코드')),
                ('kor_co_nm', models.CharField(max_length=100, verbose_name='금융회사 명')),
                ('fin_prdt_nm', models.CharField(max_length=100, verbose_name='금융 상품명')),
                ('join_way', models.CharField(max_length=200, verbose_name='가입 방법')),
                ('loan_inci_expn', models.TextField(verbose_name='대출 부대비용')),
                ('erly_rpay_fee', models.CharField(max_length=200, verbose_name='조기 상환 수수료')),
                ('dly_rate', models.TextField(verbose_name='연체 이자율')),
                ('loan_lmt', models.CharField(max_length=200, verbose_name='대출 한도')),
                ('dcls_strt_day', models.CharField(max_length=10, verbose_name='공시 시작일 [YYYY-MM-DD]')),
                ('dcls_end_day', models.CharField(blank=True, max_length=10, null=True, verbose_name='공시 종료일 [YYYY-MM-DD]')),
                ('fin_co_subm_day', models.CharField(max_length=20, verbose_name='금융회사 제출일 [YYYYMMDDHH24MI]')),
                ('fin_co_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.bank')),
            ],
        ),
        migrations.CreateModel(
            name='RentLoanProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=6, verbose_name='공시 제출월 [YYYYMM]')),
                ('fin_co_no', models.CharField(max_length=20, verbose_name='금융회사 코드')),
                ('fin_prdt_cd', models.CharField(max_length=20, verbose_name='금융상품 코드')),
                ('rpay_type', models.CharField(max_length=20, verbose_name='상환방식')),
                ('rpay_type_nm', models.CharField(max_length=100, verbose_name='상환방식명')),
                ('lend_rate_type', models.CharField(max_length=20, verbose_name='금리유형')),
                ('lend_rate_type_nm', models.CharField(max_length=100, verbose_name='금리유형명')),
                ('lend_rate_min', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='최소 금리')),
                ('lend_rate_max', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='최대 금리')),
                ('lend_rate_avg', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='평균 금리')),
                ('rent_loan_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_loan_options', to='products.rentloanproduct')),
            ],
            options={
                'verbose_name': '전세대출 상품 옵션',
                'verbose_name_plural': '전세대출 상품 옵션 목록',
            },
        ),
        migrations.CreateModel(
            name='SavingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.CharField(max_length=40, unique=True)),
                ('kor_co_nm', models.CharField(max_length=100)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('join_way', models.CharField(max_length=200)),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.CharField(max_length=20)),
                ('join_member', models.CharField(max_length=100)),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField(blank=True, null=True)),
                ('dcls_strt_day', models.CharField(max_length=10)),
                ('dcls_end_day', models.CharField(blank=True, max_length=10, null=True)),
                ('dcls_month', models.CharField(max_length=6)),
                ('fin_co_subm_day', models.CharField(max_length=20)),
                ('fin_co_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.bank')),
            ],
        ),
        migrations.CreateModel(
            name='SavingProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intr_rate_type', models.CharField(max_length=100, verbose_name='저축 금리 유형')),
                ('intr_rate_type_nm', models.CharField(max_length=100, verbose_name='저축 금리 유형명')),
                ('rsrv_type', models.CharField(max_length=100, verbose_name='적립 유형')),
                ('rsrv_type_nm', models.CharField(max_length=100, verbose_name='적립 유형명')),
                ('save_trm', models.IntegerField(help_text='단위: 개월', verbose_name='저축 기간')),
                ('intr_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='저축 금리')),
                ('intr_rate2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='최고 우대금리')),
                ('saving_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saving_options', to='products.savingproduct')),
            ],
            options={
                'verbose_name': '저축 상품 옵션',
                'verbose_name_plural': '저축 상품 옵션 목록',
            },
        ),
        migrations.CreateModel(
            name='BankOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_cd', models.CharField(max_length=2)),
                ('area_nm', models.CharField(max_length=50)),
                ('exis_yn', models.CharField(max_length=1)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='products.bank')),
            ],
        ),
        migrations.CreateModel(
            name='UserSavingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=10)),
                ('join_date', models.DateField()),
                ('saving_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.savingproduct')),
                ('selected_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.savingproductoption')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saving_products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'saving_product')},
            },
        ),
        migrations.CreateModel(
            name='UserRentLoanProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=10)),
                ('join_date', models.DateField()),
                ('rent_loan_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.rentloanproduct')),
                ('selected_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.rentloanproductoption')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_loan_products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'rent_loan_product')},
            },
        ),
        migrations.CreateModel(
            name='UserPensionProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=10)),
                ('join_date', models.DateField()),
                ('pension_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.pensionproduct')),
                ('selected_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.pensionproductoption')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pension_products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'pension_product')},
            },
        ),
        migrations.CreateModel(
            name='UserDepositProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=10)),
                ('join_date', models.DateField()),
                ('deposit_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.depositproduct')),
                ('selected_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.depositproductoption')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'deposit_product')},
            },
        ),
    ]
