from rest_framework import serializers

class DocumentSerializer(serializers.Serializer):
	def restore_object(self, attrs, instance=None):
		if instance is not None:
			for k, v in attrs.iteritems():
				setattr(instance, k, v)
			return instance
		return School(**attrs)

class EmbeddedDocumentSerializer(serializers.Serializer):
	def to_native(self, obj):
		ret = {}
		print obj
		for k in obj:
			if obj[k] is not None:
				ret[k] = obj[k]
		return ret

class EmbeddedDocumentListSerializer(serializers.Serializer):
	def to_native(self, objects):
		ret = []
		print objects
		for obj in objects:
			attrs = {}
			for k in obj:
				if obj[k] is not None:
					attrs[k] = obj[k]
			ret.append(attrs)
		return ret

class LocationSerializer(EmbeddedDocumentSerializer):
	address = serializers.CharField()
	apt = serializers.CharField()
	unit = serializers.CharField()
	city = serializers.CharField()
	region = serializers.CharField()
	postalCode = serializers.CharField()
	country = serializers.CharField()
	longitude = serializers.DecimalField()
	latitude = serializers.DecimalField()

	def field_to_native(self, obj, field_name):
		if obj is None or obj.location is None:
			return None
		return self.to_native(obj.location)

class MetaSerializer(EmbeddedDocumentSerializer):
	dateModified = serializers.DateField(required=False)
	dateCreated = serializers.DateField(required=False)
	yearValid = serializers.IntegerField()

	def field_to_native(self, obj, field_name):
		if obj is None or obj.metaData is None:
			return None
		return self.to_native(obj.metaData)

class ContactSerializer(EmbeddedDocumentSerializer):
	name = serializers.CharField()
	email = serializers.EmailField()
	phoneNumber = serializers.CharField()
	ext = serializers.CharField()
	fax = serializers.CharField()
	website = serializers.URLField()
	facebook = serializers.URLField()
	twitter = serializers.URLField()
	linkedin = serializers.URLField()
	
	def field_to_native(self, obj, field_name):
		if obj is None or obj.contact is None:
			return None
		return self.to_native(obj.contact)

class ImageSerializer(EmbeddedDocumentListSerializer):
	descriptor = serializers.CharField()
	link = serializers.URLField()

	def field_to_native(self, obj, field_name):
		if obj is None or obj.images is None:
			return None
		return self.to_native(obj.images)

class RankingSerializer(EmbeddedDocumentListSerializer):
	year = serializers.IntegerField()
	rank = serializers.IntegerField()
	source = serializers.CharField()
	title = serializers.CharField()
	link = serializers.URLField()

	def field_to_native(self, obj, field_name):
		if obj is None or obj.rankings is None:
			return None
		return self.to_native(obj.rankings)

class GenericSerializer(DocumentSerializer):
	
	id = serializers.CharField()
	shortName = serializers.CharField()
	name = serializers.CharField()
	slug = serializers.CharField(required=False)
	about = serializers.CharField()
	avgAdm = serializers.DecimalField()
	undergradPopulation = serializers.IntegerField()
	gradPopulation = serializers.IntegerField()

	metaData = MetaSerializer()
	contact = ContactSerializer()
	location = LocationSerializer()
	rankings = RankingSerializer(required=False)
	images = ImageSerializer(required=False)
