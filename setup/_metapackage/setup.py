import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-product-attribute",
    description="Meta package for oca-product-attribute Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-base_product_mass_addition',
        'odoo14-addon-packaging_uom',
        'odoo14-addon-pos_product_cost_security',
        'odoo14-addon-product_assortment',
        'odoo14-addon-product_attribute_archive',
        'odoo14-addon-product_barcode_required',
        'odoo14-addon-product_bom_revision',
        'odoo14-addon-product_category_active',
        'odoo14-addon-product_category_code',
        'odoo14-addon-product_category_code_unique',
        'odoo14-addon-product_category_product_link',
        'odoo14-addon-product_category_type',
        'odoo14-addon-product_code_mandatory',
        'odoo14-addon-product_code_unique',
        'odoo14-addon-product_cost_security',
        'odoo14-addon-product_dimension',
        'odoo14-addon-product_form_pricelist',
        'odoo14-addon-product_logistics_uom',
        'odoo14-addon-product_lot_sequence',
        'odoo14-addon-product_main_supplierinfo',
        'odoo14-addon-product_manufacturer',
        'odoo14-addon-product_medical',
        'odoo14-addon-product_model_viewer',
        'odoo14-addon-product_multi_category',
        'odoo14-addon-product_net_weight',
        'odoo14-addon-product_order_noname',
        'odoo14-addon-product_packaging_dimension',
        'odoo14-addon-product_packaging_type',
        'odoo14-addon-product_packaging_type_pallet',
        'odoo14-addon-product_packaging_type_required',
        'odoo14-addon-product_packaging_unit_price_calculator',
        'odoo14-addon-product_pricelist_button_box',
        'odoo14-addon-product_pricelist_direct_print',
        'odoo14-addon-product_pricelist_revision',
        'odoo14-addon-product_pricelist_supplierinfo',
        'odoo14-addon-product_profile',
        'odoo14-addon-product_sale_manufactured_for',
        'odoo14-addon-product_seasonality',
        'odoo14-addon-product_secondary_unit',
        'odoo14-addon-product_sequence',
        'odoo14-addon-product_state',
        'odoo14-addon-product_state_active',
        'odoo14-addon-product_state_history',
        'odoo14-addon-product_status',
        'odoo14-addon-product_stock_state',
        'odoo14-addon-product_supplierinfo_for_customer',
        'odoo14-addon-product_supplierinfo_revision',
        'odoo14-addon-product_template_tags',
        'odoo14-addon-product_template_tags_code',
        'odoo14-addon-product_tier_validation',
        'odoo14-addon-product_total_weight_from_packaging',
        'odoo14-addon-product_uom_updatable',
        'odoo14-addon-product_variant_attribute_name_manager',
        'odoo14-addon-product_video_link',
        'odoo14-addon-product_weight',
        'odoo14-addon-product_weight_logistics_uom',
        'odoo14-addon-purchase_product_template_tags',
        'odoo14-addon-sale_product_template_tags',
        'odoo14-addon-stock_product_template_tags',
        'odoo14-addon-uom_extra_data',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
