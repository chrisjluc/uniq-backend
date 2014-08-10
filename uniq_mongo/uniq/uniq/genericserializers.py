from rest_framework import serializers

class DocumentSerializer(serializers.Serializer):
	def build_instance(self, attrs):
		for k, v in attrs.iteritems():
			setattr(instance, k, v)
		return instance

class EmbeddedDocumentSerializer(serializers.Serializer):
	def to_native(self, obj):
		ret = {}
		for k in obj:
			if obj[k] is not None:
				ret[k] = obj[k]
		return ret

class EmbeddedDocumentListSerializer(serializers.Serializer):
	def to_native(self, objects):
		ret = []
		for obj in objects:
			attrs = {}
			for k in obj:
				if obj[k] is not None:
					attrs[k] = obj[k]
			ret.append(attrs)
		return ret

class ListSerializer(serializers.Serializer):
	def to_native(self, objects):
		ret = []
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

class ContactSerializer(EmbeddedDocumentListSerializer):
	name = serializers.CharField()
	email = serializers.EmailField()
	phoneNum = serializers.CharField()
	ext = serializers.CharField()
	fax = serializers.CharField()
	website = serializers.URLField()
	facebook = serializers.URLField()
	twitter = serializers.URLField()
	linkedin = serializers.URLField()
	extraInfo = serializers.CharField()

	def field_to_native(self, obj, field_name):
		if obj is None or obj.contacts is None:
			return None
		return self.to_native(obj.contacts)

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

class StreamSerializer(EmbeddedDocumentListSerializer):
	title = serializers.CharField()

	def field_to_native(self, obj, field_name):
		if obj is None or obj.streams is None:
			return None
		return self.to_native(obj.streams)

class FeeSerializer(EmbeddedDocumentSerializer):
	def field_to_native(self, obj, field_name):
		if obj is None or obj.fees is None:
			return None
		return self.to_native(obj.fees)

class ImportantDateSerializer(EmbeddedDocumentListSerializer):
	date = serializers.CharField()
	type = serializers.CharField()
	description = serializers.CharField()

	def field_to_native(self, obj, field_name):
		if obj is None or obj.importantDates is None:
			return None
		return self.to_native(obj.importantDates)

class GenericSerializer(DocumentSerializer):
	
	id = serializers.CharField()
	shortName = serializers.CharField()
	name = serializers.CharField()
	about = serializers.CharField()
	avgAdm = serializers.CharField()
	undergradPopulation = serializers.CharField()
	gradPopulation = serializers.CharField()

	metaData = MetaSerializer()
	contacts = ContactSerializer()
	location = LocationSerializer()
	rankings = RankingSerializer()
	images = ImageSerializer()
