from app.blueprint import bp

@bp.route('/bp_test')
def bp_test():
    return "BP TEST: BP WORKING"